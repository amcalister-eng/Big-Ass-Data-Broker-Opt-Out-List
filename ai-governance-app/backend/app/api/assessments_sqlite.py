import asyncio
from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.services import graph_service_sqlite as gs, llm_analyser
from app.services.scoring import confidence_to_risk_rating, compute_rai_score, aggregate_domain_scores
from app.services.document_parser import chunk_text

router = APIRouter()

BATCH_SIZE = 10


async def run_assessment(assessment_id: str, project_id: str):
    gs.update_assessment(assessment_id, status="processing")

    project = gs.get_project(project_id)
    if not project or not project.get("document_text"):
        gs.update_assessment(assessment_id, status="failed")
        return

    project_text = project["document_text"]
    questions = gs.get_all_questions()

    chunks = chunk_text(project_text)[:2]
    combined_text = "\n\n---\n\n".join(chunks)

    coverages = []
    for i in range(0, len(questions), BATCH_SIZE):
        batch = questions[i: i + BATCH_SIZE]
        try:
            results = await llm_analyser.analyse_against_questions(combined_text, batch)
        except Exception:
            results = []

        for res in results:
            q = next((q for q in batch if q["question_id"] == res["question_id"]), None)
            weight = float(q.get("risk_weight") or 5.0) if q else 5.0
            conf = float(res.get("confidence", 0.0))
            risk = confidence_to_risk_rating(conf, weight)
            gs.store_coverage(
                assessment_id, res["question_id"],
                conf, res.get("evidence"), res.get("gap_summary"), risk.value,
            )
            coverages.append({"domain": q["domain"] if q else "Unknown", "confidence": conf})

    try:
        rai_result = await llm_analyser.calculate_rai_scorecard(project_text)
        rai_meta = compute_rai_score(
            rai_result.get("triggered_factors", []),
            rai_result.get("mitigating_factors", []),
        )
    except Exception:
        rai_meta = {"total_score": 0.0, "risk_tier": "low", "requires_adrb": False, "requires_ai_council": False}

    overall_conf = sum(c["confidence"] for c in coverages) / max(len(coverages), 1)

    gs.update_assessment(
        assessment_id,
        status="complete",
        rai_score=rai_meta["total_score"],
        risk_tier=rai_meta["risk_tier"],
        requires_adrb=int(rai_meta["requires_adrb"]),
        requires_ai_council=int(rai_meta["requires_ai_council"]),
        overall_confidence=overall_conf,
    )


@router.post("/{project_id}/start")
async def start_assessment(project_id: str, background_tasks: BackgroundTasks):
    project = gs.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    assessment = gs.create_assessment(project_id)
    background_tasks.add_task(run_assessment, assessment["id"], project_id)
    return assessment


@router.get("/{assessment_id}")
async def get_assessment(assessment_id: str):
    assessment = gs.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return assessment


@router.get("/{assessment_id}/graph")
async def get_graph(assessment_id: str):
    return gs.get_graph_data(assessment_id)


@router.get("/{assessment_id}/gaps")
async def get_gaps(assessment_id: str):
    return gs.get_gaps(assessment_id)
