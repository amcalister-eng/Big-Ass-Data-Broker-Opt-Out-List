"""
PDF gap report generation using WeasyPrint + Jinja2.
"""
import os
from pathlib import Path
from datetime import datetime, timezone
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from app.models.schemas import RiskRating

TEMPLATE_DIR = Path(__file__).parent.parent / "templates"


def _risk_badge_class(rating: str) -> str:
    return {
        "critical": "badge-critical",
        "high": "badge-high",
        "medium": "badge-medium",
        "low": "badge-low",
        "not_applicable": "badge-na",
    }.get(rating, "badge-low")


def _confidence_pct(conf: float) -> str:
    return f"{int(conf * 100)}%"


def generate_pdf_report(
    project_name: str,
    assessment_id: str,
    rai_score: float,
    risk_tier: str,
    domain_scores: dict[str, float],
    gaps: list[dict],
    strengths: list[str],
    next_steps: list[str],
    output_path: str,
) -> str:
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
    env.filters["risk_badge"] = _risk_badge_class
    env.filters["confidence_pct"] = _confidence_pct

    template = env.get_template("report.html")

    html_content = template.render(
        project_name=project_name,
        assessment_id=assessment_id,
        generated_at=datetime.now(timezone.utc).strftime("%d %B %Y %H:%M UTC"),
        rai_score=rai_score,
        risk_tier=risk_tier,
        domain_scores=domain_scores,
        gaps=gaps,
        strengths=strengths,
        next_steps=next_steps,
        total_questions=len(gaps) + len(strengths),
        gap_count=len(gaps),
        coverage_pct=int((len(strengths) / max(len(gaps) + len(strengths), 1)) * 100),
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    HTML(string=html_content, base_url=str(TEMPLATE_DIR)).write_pdf(output_path)
    return output_path
