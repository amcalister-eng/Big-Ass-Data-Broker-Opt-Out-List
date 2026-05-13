import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.services import graph_service_sqlite as gs, report_generator
from app.services.scoring import aggregate_domain_scores
from app.core.config import settings

router = APIRouter()


@router.get("/{assessment_id}/pdf")
async def download_pdf(assessment_id: str):
    assessment = gs.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    if assessment.get("status") != "complete":
        raise HTTPException(status_code=400, detail="Assessment not yet complete")

    project = gs.get_project(assessment["project_id"])
    project_name = project["name"] if project else "Unknown Project"

    gaps = gs.get_gaps(assessment_id)
    coverages = gs.get_all_coverages(assessment_id)
    domain_scores = aggregate_domain_scores(coverages)

    strengths = [c for c in coverages if c.get("confidence", 0) >= 0.8]
    next_steps = list({g["patterns"][0] for g in gaps if g.get("patterns")})[:5]
    if not next_steps:
        next_steps = [
            "Complete Privacy Impact Assessment",
            "Engage AI Council for review",
            "Document model card",
        ]

    report_dir = os.path.join(settings.upload_dir, "reports")
    os.makedirs(report_dir, exist_ok=True)
    output_path = os.path.join(report_dir, f"{assessment_id}.pdf")

    try:
        pdf_path = report_generator.generate_pdf_report(
            project_name=project_name,
            assessment_id=assessment_id,
            rai_score=float(assessment.get("rai_score") or 0),
            risk_tier=assessment.get("risk_tier") or "low",
            domain_scores=domain_scores,
            gaps=gaps,
            strengths=[f"{s['domain']} — {int(s['confidence']*100)}% coverage" for s in strengths[:10]],
            next_steps=next_steps,
            output_path=output_path,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF generation failed: {str(e)}")

    safe_name = project_name.replace(" ", "_")[:40]
    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=f"governance_gap_report_{safe_name}.pdf",
    )
