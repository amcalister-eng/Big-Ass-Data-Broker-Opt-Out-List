"""
Neo4j graph operations for projects and assessments.
"""
from datetime import datetime, timezone
import uuid
from neo4j import AsyncSession


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


async def create_project(session: AsyncSession, name: str, description: str, team: str = "", business_unit: str = "") -> dict:
    project_id = str(uuid.uuid4())
    await session.run(
        """
        CREATE (p:Project {
            id: $id, name: $name, description: $description,
            team: $team, business_unit: $business_unit, created_at: $created_at
        })
        """,
        id=project_id, name=name, description=description,
        team=team or "", business_unit=business_unit or "", created_at=_now(),
    )
    return {"id": project_id, "name": name, "description": description, "team": team, "business_unit": business_unit, "created_at": _now()}


async def get_project(session: AsyncSession, project_id: str) -> dict | None:
    result = await session.run("MATCH (p:Project {id: $id}) RETURN p", id=project_id)
    record = await result.single()
    if record:
        return dict(record["p"])
    return None


async def list_projects(session: AsyncSession) -> list[dict]:
    result = await session.run("MATCH (p:Project) RETURN p ORDER BY p.created_at DESC")
    records = await result.data()
    return [dict(r["p"]) for r in records]


async def create_assessment(session: AsyncSession, project_id: str) -> dict:
    assessment_id = str(uuid.uuid4())
    await session.run(
        """
        MATCH (p:Project {id: $project_id})
        CREATE (a:ProjectAssessment {
            id: $id, project_id: $project_id, status: 'pending', created_at: $created_at
        })-[:ASSESSES]->(p)
        """,
        id=assessment_id, project_id=project_id, created_at=_now(),
    )
    return {"id": assessment_id, "project_id": project_id, "status": "pending", "created_at": _now()}


async def update_assessment_status(session: AsyncSession, assessment_id: str, status: str, **kwargs):
    set_clauses = ["a.status = $status"]
    params = {"assessment_id": assessment_id, "status": status}
    for k, v in kwargs.items():
        set_clauses.append(f"a.{k} = ${k}")
        params[k] = v
    if status == "complete":
        set_clauses.append("a.completed_at = $completed_at")
        params["completed_at"] = _now()
    query = f"MATCH (a:ProjectAssessment {{id: $assessment_id}}) SET {', '.join(set_clauses)}"
    await session.run(query, **params)


async def store_node_coverage(
    session: AsyncSession,
    assessment_id: str,
    question_id: str,
    confidence: float,
    evidence: str | None,
    gap_summary: str | None,
    risk_rating: str,
):
    await session.run(
        """
        MATCH (a:ProjectAssessment {id: $assessment_id})
        MATCH (q:AssessmentQuestion {id: $question_id})
        MERGE (a)-[r:COVERS]->(q)
        SET r.confidence = $confidence,
            r.evidence = $evidence,
            r.gap_summary = $gap_summary,
            r.risk_rating = $risk_rating,
            r.updated_at = $updated_at
        """,
        assessment_id=assessment_id,
        question_id=question_id,
        confidence=confidence,
        evidence=evidence or "",
        gap_summary=gap_summary or "",
        risk_rating=risk_rating,
        updated_at=_now(),
    )


async def get_graph_data(session: AsyncSession, assessment_id: str) -> dict:
    """Return nodes and edges for Cytoscape.js visualisation."""
    # Get the assessment and connected nodes
    node_result = await session.run(
        """
        MATCH (a:ProjectAssessment {id: $id})-[r:COVERS]->(q:AssessmentQuestion)
        MATCH (q)-[:BELONGS_TO]->(d:RiskDomain)
        OPTIONAL MATCH (q)-[:MAPS_TO]->(s:StandardClause)
        RETURN q.id AS qid, q.text AS qtext, q.risk_weight AS weight,
               d.id AS domain_id, d.name AS domain_name, d.color AS domain_color,
               r.confidence AS confidence, r.risk_rating AS risk_rating,
               r.gap_summary AS gap_summary,
               collect(s.standard_id) AS standards
        """,
        id=assessment_id,
    )

    nodes = []
    edges = []
    domain_ids_seen = set()
    records = await node_result.data()

    for rec in records:
        domain_id = rec["domain_id"]
        if domain_id not in domain_ids_seen:
            domain_ids_seen.add(domain_id)
            nodes.append({
                "data": {
                    "id": domain_id,
                    "label": rec["domain_name"],
                    "type": "domain",
                    "color": rec["domain_color"] or "#6366f1",
                }
            })

        conf = rec["confidence"] or 0.0
        nodes.append({
            "data": {
                "id": rec["qid"],
                "label": rec["qtext"][:60] + ("..." if len(rec["qtext"]) > 60 else ""),
                "type": "question",
                "confidence": conf,
                "risk_rating": rec["risk_rating"] or "low",
                "gap_summary": rec["gap_summary"] or "",
                "standards": rec["standards"] or [],
                "color": _confidence_color(conf),
            }
        })
        edges.append({
            "data": {
                "id": f"e-{domain_id}-{rec['qid']}",
                "source": domain_id,
                "target": rec["qid"],
                "weight": conf,
            }
        })

    return {"nodes": nodes, "edges": edges}


def _confidence_color(confidence: float) -> str:
    if confidence >= 0.8:
        return "#22c55e"   # green
    elif confidence >= 0.5:
        return "#f59e0b"   # amber
    else:
        return "#ef4444"   # red


async def get_assessment_gaps(session: AsyncSession, assessment_id: str) -> list[dict]:
    result = await session.run(
        """
        MATCH (a:ProjectAssessment {id: $id})-[r:COVERS]->(q:AssessmentQuestion)
        WHERE r.confidence < 0.8
        MATCH (q)-[:BELONGS_TO]->(d:RiskDomain)
        OPTIONAL MATCH (q)-[:HAS_CONTROL]->(cr:ControlRecommendation)
        OPTIONAL MATCH (q)-[:FOLLOWS_PATTERN]->(gp:GovernancePattern)
        OPTIONAL MATCH (q)-[:MAPS_TO]->(sc:StandardClause)
        RETURN q.id AS question_id, q.text AS question_text,
               d.name AS domain,
               r.confidence AS confidence,
               r.risk_rating AS risk_rating,
               r.gap_summary AS gap_description,
               collect(DISTINCT cr.description) AS controls,
               collect(DISTINCT gp.name) AS patterns,
               collect(DISTINCT sc.standard_id) AS standards
        ORDER BY r.confidence ASC
        """,
        id=assessment_id,
    )
    return await result.data()


async def get_assessment(session: AsyncSession, assessment_id: str) -> dict | None:
    result = await session.run(
        "MATCH (a:ProjectAssessment {id: $id}) RETURN a",
        id=assessment_id,
    )
    record = await result.single()
    return dict(record["a"]) if record else None


async def get_all_questions(session: AsyncSession) -> list[dict]:
    result = await session.run(
        """
        MATCH (q:AssessmentQuestion)-[:BELONGS_TO]->(d:RiskDomain)
        RETURN q.id AS question_id, q.text AS question_text,
               q.risk_weight AS risk_weight, d.name AS domain
        ORDER BY d.name, q.id
        """
    )
    return await result.data()
