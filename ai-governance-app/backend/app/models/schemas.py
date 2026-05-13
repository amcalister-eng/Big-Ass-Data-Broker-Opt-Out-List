from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class RiskRating(str, Enum):
    critical = "critical"
    high = "high"
    medium = "medium"
    low = "low"
    not_applicable = "not_applicable"


class ProjectCreate(BaseModel):
    name: str
    description: str
    team: Optional[str] = None
    business_unit: Optional[str] = None


class ProjectOut(ProjectCreate):
    id: str
    created_at: str


class AssessmentStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    complete = "complete"
    failed = "failed"


class AssessmentOut(BaseModel):
    id: str
    project_id: str
    status: AssessmentStatus
    rai_score: Optional[float] = None
    overall_risk: Optional[RiskRating] = None
    created_at: str
    completed_at: Optional[str] = None


class NodeCoverage(BaseModel):
    node_id: str
    node_type: str
    label: str
    domain: str
    confidence: float = Field(ge=0.0, le=1.0)
    risk_rating: RiskRating
    evidence: Optional[str] = None
    gap_summary: Optional[str] = None


class GraphData(BaseModel):
    nodes: list[dict]
    edges: list[dict]


class GapItem(BaseModel):
    domain: str
    question_id: str
    question_text: str
    confidence: float
    risk_rating: RiskRating
    gap_description: str
    recommended_controls: list[str]
    governance_patterns: list[str]
    standards_references: list[str]


class AssessmentReport(BaseModel):
    project_name: str
    assessment_id: str
    rai_score: float
    overall_risk: RiskRating
    domain_scores: dict[str, float]
    gaps: list[GapItem]
    strengths: list[str]
    next_steps: list[str]


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    project_id: str
    message: str
    history: list[ChatMessage] = []


class ChatResponse(BaseModel):
    response: str
    sources: list[str] = []


class RAIScorecardResult(BaseModel):
    total_score: float
    risk_tier: str
    triggered_factors: list[dict]
    mitigating_factors: list[dict]
    requires_adrb: bool
    requires_ai_council: bool
