// ── Supplier & Third Party Questions ─────────────────────────────────────────
MATCH (d:RiskDomain {id: 'RD-SUP'})

MERGE (q:AssessmentQuestion {id: 'SUP-01'})
  SET q.text = 'Has a Supplier Risk Assessment been completed for all AI vendors and model providers?',
      q.domain = 'Supplier & Third Party', q.risk_weight = 8.0, q.category = 'Supplier';
MERGE (q)-[:BELONGS_TO]->(d)

MERGE (q2:AssessmentQuestion {id: 'SUP-02'})
  SET q2.text = 'Are data processing agreements (DPAs) or AI-specific addenda in place with all AI suppliers?',
      q2.domain = 'Supplier & Third Party', q2.risk_weight = 8.0, q2.category = 'Supplier';
MERGE (q2)-[:BELONGS_TO]->(d)

MERGE (q3:AssessmentQuestion {id: 'SUP-03'})
  SET q3.text = 'Does the supplier retain training rights over data submitted to their models?',
      q3.domain = 'Supplier & Third Party', q3.risk_weight = 9.0, q3.category = 'Supplier';
MERGE (q3)-[:BELONGS_TO]->(d)

MERGE (q4:AssessmentQuestion {id: 'SUP-04'})
  SET q4.text = 'Are model cards or equivalent documentation available for all third-party AI models used?',
      q4.domain = 'Supplier & Third Party', q4.risk_weight = 6.0, q4.category = 'Supplier';
MERGE (q4)-[:BELONGS_TO]->(d)

MERGE (q5:AssessmentQuestion {id: 'SUP-05'})
  SET q5.text = 'Is there a process to monitor AI supplier performance, drift, and responsible AI compliance?',
      q5.domain = 'Supplier & Third Party', q5.risk_weight = 7.0, q5.category = 'Supplier';
MERGE (q5)-[:BELONGS_TO]->(d)

MERGE (q6:AssessmentQuestion {id: 'SUP-06'})
  SET q6.text = 'Does the supplier have an established responsible/ethical AI policy?',
      q6.domain = 'Supplier & Third Party', q6.risk_weight = 7.0, q6.category = 'Supplier';
MERGE (q6)-[:BELONGS_TO]->(d)

MERGE (q7:AssessmentQuestion {id: 'SUP-07'})
  SET q7.text = 'Is there a documented exit/transition plan if the AI supplier is replaced or service is discontinued?',
      q7.domain = 'Supplier & Third Party', q7.risk_weight = 6.0, q7.category = 'Supplier';
MERGE (q7)-[:BELONGS_TO]->(d)

MERGE (q8:AssessmentQuestion {id: 'SUP-08'})
  SET q8.text = 'Has IP ownership of AI outputs been clarified with legal and the supplier contract?',
      q8.domain = 'Supplier & Third Party', q8.risk_weight = 7.0, q8.category = 'Supplier';
MERGE (q8)-[:BELONGS_TO]->(d)

MERGE (q9:AssessmentQuestion {id: 'SUP-09'})
  SET q9.text = 'Are fourth-party risks (sub-processors, cloud providers used by the AI vendor) assessed?',
      q9.domain = 'Supplier & Third Party', q9.risk_weight = 6.0, q9.category = 'Supplier';
MERGE (q9)-[:BELONGS_TO]->(d)

MERGE (q10:AssessmentQuestion {id: 'SUP-10'})
  SET q10.text = 'Is the AI supplier subject to regular security audits (SOC 2, ISO 27001, or equivalent)?',
      q10.domain = 'Supplier & Third Party', q10.risk_weight = 7.0, q10.category = 'Supplier';
MERGE (q10)-[:BELONGS_TO]->(d)
