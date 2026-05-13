import asyncio
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from neo4j import AsyncSession
from app.core.database import get_session, get_driver
from app.services import graph_service, llm_analyser
from app.services.scoring import confidence_to_risk_rating, compute_rai_score, aggregate_domain_scores
from app.services.document_parser import chunk_text

router = APIRouter()

BATCH_SIZE = 10  # questions per LLM call


async def run_assessment(assessment_id: str, project_id: str):
    """Background task: analyse project document against all governance questions."""
    driver = await get_driver()
    async with driver.session() as session:
        await graph_service.update_assessment_status(session, assessment_id, "processing")

        project = await graph_service.get_project(session, project_id)
        if not project or not project.get("document_text"):
            await graph_service.update_assessment_status(session, assessment_id, "failed")
            return

        project_text = project["document_text"]
        questions = await graph_service.get_all_questions(session)

        # Chunk project text; use first two chunks for analysis
        chunks = chunk_text(project_text)[:2]
        combined_text = "\n\n---\n\n".join(chunks)

        coverages = []
        # Process questions in batches
        for i in range(0, len(questions), BATCH_SIZE):
            batch = questions[i: i + BATCH_SIZE]
            try:
                results = await asyncio.to_thread(
                    llm_analyser.analyse_against_questions.__wrapped__
                    if hasattr(llm_analyser.analyse_against_questions, '__wrapped__')
                    else _sync_analyse,
                    combined_text, batch,
                )
            except Exception:
                results = _sync_analyse(combined_text, batch)

            for res in results:
                q = next((q for q in batch if q["question_id"] == res["question_id"]), None)
                weight = float(q.get("risk_weight") or 5.0) if q else 5.0
                conf = float(res.get("confidence", 0.0))
                risk = confidence_to_risk_rating(conf, weight)
                await graph_service.store_node_coverage(
                    session, assessment_id, res["question_id"],
                    conf, res.get("evidence"), res.get("gap_summary"), risk.value,
                )
                coverages.append({"domain": q["domain"] if q else "Unknown", "confidence": conf})

        # RAI Scorecard
        try:
            rai_result = _sync_rai(project_text)
            rai_meta = compute_rai_score(rai_result.get("triggered_factors", []), rai_result.get("mitigating_factors", []))
        except Exception:
            rai_meta = {"total_score": 0.0, "risk_tier": "low", "requires_adrb": False, "requires_ai_council": False}

        domain_scores = aggregate_domain_scores(coverages)
        overall_conf = sum(c["confidence"] for c in coverages) / max(len(coverages), 1)

        await graph_service.update_assessment_status(
            session, assessment_id, "complete",
            rai_score=rai_meta["total_score"],
            risk_tier=rai_meta["risk_tier"],
            requires_adrb=rai_meta["requires_adrb"],
            requires_ai_council=rai_meta["requires_ai_council"],
            overall_confidence=overall_conf,
        )


def _sync_analyse(project_text: str, batch: list[dict]) -> list[dict]:
    import asyncio
    return asyncio.get_event_loop().run_until_complete(
        llm_analyser.analyse_against_questions(project_text, batch)
    )


def _sync_rai(project_text: str) -> dict:
    import asyncio
    return asyncio.get_event_loop().run_until_complete(
        llm_analyser.calculate_rai_scorecard(project_text)
    )


@router.post("/{project_id}/start")
async def start_assessment(
    project_id: str,
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_session),
):
    project = await graph_service.get_project(session, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    assessment = await graph_service.create_assessment(session, project_id)
    background_tasks.add_task(run_assessment, assessment["id"], project_id)
    return assessment


@router.get("/{assessment_id}")
async def get_assessment(assessment_id: str, session: AsyncSession = Depends(get_session)):
    assessment = await graph_service.get_assessment(session, assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return assessment


@router.get("/{assessment_id}/graph")
async def get_graph(assessment_id: str, session: AsyncSession = Depends(get_session)):
    return await graph_service.get_graph_data(session, assessment_id)


@router.get("/{assessment_id}/gaps")
async def get_gaps(assessment_id: str, session: AsyncSession = Depends(get_session)):
    return await graph_service.get_assessment_gaps(session, assessment_id)
