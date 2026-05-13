// ── Agentic AI Questions ──────────────────────────────────────────────────────
MATCH (d:RiskDomain {id: 'RD-AGT'})

MERGE (q1:AssessmentQuestion {id: 'AGT-01'})
  SET q1.text = 'What is the autonomy level of the agent (human-in-the-loop, supervised, or fully autonomous)?',
      q1.domain = 'Agentic AI', q1.risk_weight = 10.0, q1.category = 'Agentic';
MERGE (q1)-[:BELONGS_TO]->(d)

MERGE (q2:AssessmentQuestion {id: 'AGT-02'})
  SET q2.text = 'Are there defined boundaries on the tools, actions and data the agent can access?',
      q2.domain = 'Agentic AI', q2.risk_weight = 9.0, q2.category = 'Agentic';
MERGE (q2)-[:BELONGS_TO]->(d)

MERGE (q3:AssessmentQuestion {id: 'AGT-03'})
  SET q3.text = 'Is there a human escalation and override mechanism for high-risk agent decisions?',
      q3.domain = 'Agentic AI', q3.risk_weight = 10.0, q3.category = 'Agentic';
MERGE (q3)-[:BELONGS_TO]->(d)

MERGE (q4:AssessmentQuestion {id: 'AGT-04'})
  SET q4.text = 'Is the agentic framework (single-agent vs multi-agent orchestration) documented and justified?',
      q4.domain = 'Agentic AI', q4.risk_weight = 7.0, q4.category = 'Agentic';
MERGE (q4)-[:BELONGS_TO]->(d)

MERGE (q5:AssessmentQuestion {id: 'AGT-05'})
  SET q5.text = 'Are the core LLMs used by the agent routed through an approved trust layer (e.g., Einstein Trust Layer)?',
      q5.domain = 'Agentic AI', q5.risk_weight = 8.0, q5.category = 'Agentic';
MERGE (q5)-[:BELONGS_TO]->(d)

MERGE (q6:AssessmentQuestion {id: 'AGT-06'})
  SET q6.text = 'Are prompt injection and adversarial attack mitigations implemented for the agent?',
      q6.domain = 'Agentic AI', q6.risk_weight = 9.0, q6.category = 'Agentic';
MERGE (q6)-[:BELONGS_TO]->(d)

MERGE (q7:AssessmentQuestion {id: 'AGT-07'})
  SET q7.text = 'Are agent reasoning traces logged and auditable?',
      q7.domain = 'Agentic AI', q7.risk_weight = 8.0, q7.category = 'Agentic';
MERGE (q7)-[:BELONGS_TO]->(d)

MERGE (q8:AssessmentQuestion {id: 'AGT-08'})
  SET q8.text = 'Are Flex Credit / compute costs estimated and monitored for the agent runtime?',
      q8.domain = 'Agentic AI', q8.risk_weight = 5.0, q8.category = 'Agentic';
MERGE (q8)-[:BELONGS_TO]->(d)

MERGE (q9:AssessmentQuestion {id: 'AGT-09'})
  SET q9.text = 'Is there a fallback/escalation path if the agent fails or produces an uncertain result?',
      q9.domain = 'Agentic AI', q9.risk_weight = 8.0, q9.category = 'Agentic';
MERGE (q9)-[:BELONGS_TO]->(d)

MERGE (q10:AssessmentQuestion {id: 'AGT-10'})
  SET q10.text = 'Has the Agentic AI COE reviewed the agent design prior to development?',
      q10.domain = 'Agentic AI', q10.risk_weight = 8.0, q10.category = 'Agentic';
MERGE (q10)-[:BELONGS_TO]->(d)

MERGE (q11:AssessmentQuestion {id: 'AGT-11'})
  SET q11.text = 'Are secrets (API keys, credentials) managed via a secrets manager and absent from agent code?',
      q11.domain = 'Agentic AI', q11.risk_weight = 9.0, q11.category = 'Agentic';
MERGE (q11)-[:BELONGS_TO]->(d)

MERGE (q12:AssessmentQuestion {id: 'AGT-12'})
  SET q12.text = 'Is the agent subject to a review cadence after deployment (e.g., monthly usage and drift review)?',
      q12.domain = 'Agentic AI', q12.risk_weight = 6.0, q12.category = 'Agentic';
MERGE (q12)-[:BELONGS_TO]->(d)

MERGE (q13:AssessmentQuestion {id: 'AGT-13'})
  SET q13.text = 'Is there an AI-generated response disclaimer presented to users interacting with the agent?',
      q13.domain = 'Agentic AI', q13.risk_weight = 7.0, q13.category = 'Agentic';
MERGE (q13)-[:BELONGS_TO]->(d)

MERGE (q14:AssessmentQuestion {id: 'AGT-14'})
  SET q14.text = 'Are toxicity detection and PII/PCI masking applied to agent inputs and outputs?',
      q14.domain = 'Agentic AI', q14.risk_weight = 8.0, q14.category = 'Agentic';
MERGE (q14)-[:BELONGS_TO]->(d)

MERGE (q15:AssessmentQuestion {id: 'AGT-15'})
  SET q15.text = 'Can existing agents or approved assets be reused rather than building a new agent from scratch?',
      q15.domain = 'Agentic AI', q15.risk_weight = 4.0, q15.category = 'Agentic';
MERGE (q15)-[:BELONGS_TO]->(d)
