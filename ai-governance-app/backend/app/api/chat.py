from fastapi import APIRouter, Depends, HTTPException
from neo4j import AsyncSession
from app.core.database import get_session
from app.models.schemas import ChatRequest, ChatResponse
from app.services import graph_service, llm_analyser

router = APIRouter()


@router.post("", response_model=ChatResponse)
async def chat(req: ChatRequest, session: AsyncSession = Depends(get_session)):
    project = await graph_service.get_project(session, req.project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project_text = project.get("document_text", project.get("description", ""))

    # Build assessment summary from gaps
    gaps = []
    result = await session.run(
        """
        MATCH (p:Project {id: $pid})<-[:ASSESSES]-(a:ProjectAssessment)
        WHERE a.status = 'complete'
        RETURN a.id AS aid ORDER BY a.created_at DESC LIMIT 1
        """,
        pid=req.project_id,
    )
    rec = await result.single()
    assessment_summary = "No completed assessment found yet."
    if rec:
        gaps = await graph_service.get_assessment_gaps(session, rec["aid"])
        if gaps:
            lines = [f"- [{g['domain']}] {g['question_text'][:80]}... (confidence {int(g['confidence']*100)}%)" for g in gaps[:10]]
            assessment_summary = "Key governance gaps:\n" + "\n".join(lines)

    conversation = [{"role": m.role, "content": m.content} for m in req.history]
    conversation.append({"role": "user", "content": req.message})

    response_text = llm_analyser.chat_with_project(project_text, assessment_summary, conversation)

    sources = list({g["domain"] for g in gaps[:5]}) if gaps else []
    return ChatResponse(response=response_text, sources=sources)
