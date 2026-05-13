"""
RAI Scorecard scoring engine and risk tier determination.
"""
from app.models.schemas import RiskRating

# Numeric risk weights from the RAI weighting document
RAI_RISK_FACTORS = {
    "LGL_EFF":    {"name": "Legal effect on person",             "score": 10},
    "HIGH_AUT":   {"name": "High autonomy / autonomous decisions", "score": 10},
    "BIO":        {"name": "Biometrics processing",              "score": 5},
    "SENSITIVE":  {"name": "Sensitive data categories",           "score": 4},
    "VULNERABLE": {"name": "Vulnerable cohorts",                 "score": 4},
    "LARGE_SCALE":{"name": "Large scale processing (>10k)",      "score": 3},
    "NEW_TECH":   {"name": "Novel or unproven technology",       "score": 3},
    "EXT_CUST":   {"name": "External customers affected",        "score": 2},
    "THIRD_PARTY":{"name": "Third party data sharing",           "score": 2},
    "REAL_TIME":  {"name": "Real-time processing",               "score": 2},
}

RAI_MITIGATING_FACTORS = {
    "HUMAN_LOOP":       {"name": "Strong human-in-the-loop",        "score": -2},
    "POC_ONLY":         {"name": "Proof of concept only",           "score": -1},
    "INTERNAL_ONLY":    {"name": "Internal staff only",             "score": -1},
    "EXISTING_APPROVAL":{"name": "Existing approved system extension","score": -1},
}

# Risk tier thresholds
RISK_TIERS = [
    (15, "critical", True, True),    # score>=15: critical, requires ADRB + AI Council
    (8,  "high",     True, False),   # score>=8:  high, requires ADRB
    (4,  "medium",   False, False),  # score>=4:  medium
    (0,  "low",      False, False),  # score>=0:  low
]


def compute_rai_score(triggered: list[dict], mitigating: list[dict]) -> dict:
    raw_score = sum(f.get("score", 0) for f in triggered)
    mitigation = sum(abs(f.get("score", 0)) for f in mitigating)
    total = max(0.0, raw_score - mitigation)

    risk_tier = "low"
    requires_adrb = False
    requires_ai_council = False
    for threshold, tier, adrb, council in RISK_TIERS:
        if total >= threshold:
            risk_tier = tier
            requires_adrb = adrb
            requires_ai_council = council
            break

    return {
        "total_score": total,
        "risk_tier": risk_tier,
        "requires_adrb": requires_adrb,
        "requires_ai_council": requires_ai_council,
    }


def confidence_to_risk_rating(confidence: float, question_risk_weight: float) -> RiskRating:
    """Map LLM confidence + question weight to a risk rating for a gap."""
    gap_severity = (1.0 - confidence) * question_risk_weight
    if gap_severity >= 8.0:
        return RiskRating.critical
    elif gap_severity >= 5.0:
        return RiskRating.high
    elif gap_severity >= 2.0:
        return RiskRating.medium
    else:
        return RiskRating.low


def aggregate_domain_scores(coverages: list[dict]) -> dict[str, float]:
    """Average confidence per domain."""
    domain_totals: dict[str, list[float]] = {}
    for cov in coverages:
        d = cov.get("domain", "Unknown")
        domain_totals.setdefault(d, []).append(cov.get("confidence", 0.0))
    return {d: sum(v) / len(v) for d, v in domain_totals.items()}
