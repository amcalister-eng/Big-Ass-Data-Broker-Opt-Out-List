from fastapi import APIRouter, HTTPException
from app.services import graph_service_sqlite as gs, llm_analyser
from app.models.schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post("")
async def chat(req: ChatRequest):
    project = gs.get_project(req.project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project_text = project.get("document_text") or project.get("description", "")

    assessment_id = gs.get_latest_assessment_for_project(req.project_id)
    assessment_summary = "No completed assessment found yet."
    gaps = []
    if assessment_id:
        gaps = gs.get_gaps(assessment_id)
        if gaps:
            lines = [
                f"- [{g['domain']}] {g['question_text'][:80]}... (confidence {int(g['confidence']*100)}%)"
                for g in gaps[:10]
            ]
            assessment_summary = "Key governance gaps:\n" + "\n".join(lines)

    conversation = [{"role": m.role, "content": m.content} for m in req.history]
    conversation.append({"role": "user", "content": req.message})

    response_text = llm_analyser.chat_with_project(project_text, assessment_summary, conversation)

    sources = list({g["domain"] for g in gaps[:5]}) if gaps else []
    return ChatResponse(response=response_text, sources=sources)
