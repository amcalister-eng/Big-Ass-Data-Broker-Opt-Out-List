"""
SQLite-backed graph service — mirrors the Neo4j graph_service API.
"""
import uuid
from datetime import datetime, timezone
from app.core.database_sqlite import get_conn


def _now():
    return datetime.now(timezone.utc).isoformat()


# ── Projects ──────────────────────────────────────────────────────────────────

def create_project(name, description, team="", business_unit=""):
    pid = str(uuid.uuid4())
    conn = get_conn()
    conn.execute(
        "INSERT INTO projects VALUES (?,?,?,?,?,?,?,?)",
        (pid, name, description, team, business_unit, "", "", _now()),
    )
    conn.commit()
    conn.close()
    return {"id": pid, "name": name, "description": description,
            "team": team, "business_unit": business_unit, "created_at": _now()}


def store_document_text(project_id, text, file_name):
    conn = get_conn()
    conn.execute(
        "UPDATE projects SET document_text=?, file_name=? WHERE id=?",
        (text[:50000], file_name, project_id),
    )
    conn.commit()
    conn.close()


def get_project(project_id):
    conn = get_conn()
    row = conn.execute("SELECT * FROM projects WHERE id=?", (project_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def list_projects():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM projects ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ── Assessments ───────────────────────────────────────────────────────────────

def create_assessment(project_id):
    aid = str(uuid.uuid4())
    conn = get_conn()
    conn.execute(
        "INSERT INTO assessments VALUES (?,?,?,?,?,?,?,?,?,?)",
        (aid, project_id, "pending", None, None, None, 0, 0, _now(), None),
    )
    conn.commit()
    conn.close()
    return {"id": aid, "project_id": project_id, "status": "pending", "created_at": _now()}


def update_assessment(assessment_id, **kwargs):
    if not kwargs:
        return
    conn = get_conn()
    sets = ", ".join(f"{k}=?" for k in kwargs)
    vals = list(kwargs.values()) + [assessment_id]
    conn.execute(f"UPDATE assessments SET {sets} WHERE id=?", vals)
    conn.commit()
    conn.close()


def get_assessment(assessment_id):
    conn = get_conn()
    row = conn.execute("SELECT * FROM assessments WHERE id=?", (assessment_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def get_all_questions():
    conn = get_conn()
    rows = conn.execute(
        "SELECT id AS question_id, text AS question_text, risk_weight, domain FROM questions"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def store_coverage(assessment_id, question_id, confidence, evidence, gap_summary, risk_rating):
    conn = get_conn()
    conn.execute(
        "INSERT OR REPLACE INTO coverage VALUES (?,?,?,?,?,?)",
        (assessment_id, question_id, confidence, evidence or "", gap_summary or "", risk_rating),
    )
    conn.commit()
    conn.close()


def get_graph_data(assessment_id):
    conn = get_conn()
    rows = conn.execute("""
        SELECT q.id AS qid, q.text AS qtext, q.domain AS domain_name,
               d.id AS domain_id, d.color AS domain_color,
               c.confidence, c.risk_rating, c.gap_summary
        FROM coverage c
        JOIN questions q ON q.id = c.question_id
        JOIN risk_domains d ON d.name = q.domain
        WHERE c.assessment_id = ?
    """, (assessment_id,)).fetchall()
    conn.close()

    nodes = []
    edges = []
    seen_domains = set()

    def color(conf):
        if conf >= 0.8: return "#22c55e"
        if conf >= 0.5: return "#f59e0b"
        return "#ef4444"

    for r in rows:
        did = r["domain_id"]
        if did not in seen_domains:
            seen_domains.add(did)
            nodes.append({"data": {"id": did, "label": r["domain_name"],
                                   "type": "domain", "color": r["domain_color"] or "#6366f1"}})
        conf = r["confidence"] or 0.0
        nodes.append({"data": {"id": r["qid"],
                                "label": r["qtext"][:60] + ("..." if len(r["qtext"]) > 60 else ""),
                                "type": "question", "confidence": conf,
                                "risk_rating": r["risk_rating"] or "low",
                                "gap_summary": r["gap_summary"] or "",
                                "color": color(conf)}})
        edges.append({"data": {"id": f"e-{did}-{r['qid']}", "source": did, "target": r["qid"]}})

    return {"nodes": nodes, "edges": edges}


def get_gaps(assessment_id):
    conn = get_conn()
    rows = conn.execute("""
        SELECT q.id AS question_id, q.text AS question_text, q.domain AS domain,
               c.confidence, c.risk_rating, c.gap_summary AS gap_description
        FROM coverage c
        JOIN questions q ON q.id = c.question_id
        WHERE c.assessment_id = ? AND c.confidence < 0.8
        ORDER BY c.confidence ASC
    """, (assessment_id,)).fetchall()

    result = []
    for r in rows:
        d = dict(r)
        # Fetch controls
        ctrl_rows = conn.execute("""
            SELECT cr.description FROM control_recommendations cr
            JOIN question_controls qc ON qc.control_id = cr.id
            WHERE qc.question_id = ?
        """, (r["question_id"],)).fetchall()
        d["controls"] = [c["description"] for c in ctrl_rows]

        # Fetch patterns
        pat_rows = conn.execute("""
            SELECT gp.name FROM governance_patterns gp
            JOIN question_patterns qp ON qp.pattern_id = gp.id
            WHERE qp.question_id = ?
        """, (r["question_id"],)).fetchall()
        d["patterns"] = [p["name"] for p in pat_rows]

        # Fetch standards
        std_rows = conn.execute("""
            SELECT sc.standard_id FROM standard_clauses sc
            JOIN question_standards qs ON qs.clause_id = sc.id
            WHERE qs.question_id = ?
        """, (r["question_id"],)).fetchall()
        d["standards"] = [s["standard_id"] for s in std_rows]
        result.append(d)

    conn.close()
    return result


def get_all_coverages(assessment_id):
    conn = get_conn()
    rows = conn.execute("""
        SELECT q.domain, c.confidence FROM coverage c
        JOIN questions q ON q.id = c.question_id
        WHERE c.assessment_id = ?
    """, (assessment_id,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_latest_assessment_for_project(project_id):
    conn = get_conn()
    row = conn.execute(
        "SELECT id FROM assessments WHERE project_id=? AND status='complete' ORDER BY created_at DESC LIMIT 1",
        (project_id,)
    ).fetchone()
    conn.close()
    return row["id"] if row else None
