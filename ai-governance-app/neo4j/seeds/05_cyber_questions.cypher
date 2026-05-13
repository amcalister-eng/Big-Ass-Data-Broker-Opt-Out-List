// ── Cyber Security Questions (CIS8-aligned) ───────────────────────────────────
MATCH (d:RiskDomain {id: 'RD-CYB'})

MERGE (q1:AssessmentQuestion {id: 'CYB-01'})
  SET q1.text = 'Is an inventory of hardware and software assets that process AI model data maintained? (CIS8-1/2)',
      q1.domain = 'Cyber Security', q1.risk_weight = 6.0, q1.category = 'Cyber';
MERGE (q1)-[:BELONGS_TO]->(d)

MERGE (q2:AssessmentQuestion {id: 'CYB-02'})
  SET q2.text = 'Are data flows for AI inputs/outputs documented and classified by sensitivity? (CIS8-3)',
      q2.domain = 'Cyber Security', q2.risk_weight = 7.0, q2.category = 'Cyber';
MERGE (q2)-[:BELONGS_TO]->(d)

MERGE (q3:AssessmentQuestion {id: 'CYB-03'})
  SET q3.text = 'Are accounts accessing AI infrastructure protected with MFA and least-privilege access? (CIS8-5/6)',
      q3.domain = 'Cyber Security', q3.risk_weight = 8.0, q3.category = 'Cyber';
MERGE (q3)-[:BELONGS_TO]->(d)

MERGE (q4:AssessmentQuestion {id: 'CYB-04'})
  SET q4.text = 'Is data used for AI training/inference encrypted at rest and in transit? (CIS8-3)',
      q4.domain = 'Cyber Security', q4.risk_weight = 8.0, q4.category = 'Cyber';
MERGE (q4)-[:BELONGS_TO]->(d)

MERGE (q5:AssessmentQuestion {id: 'CYB-05'})
  SET q5.text = 'Is API access to AI models secured with key management and rate limiting? (CIS8-4)',
      q5.domain = 'Cyber Security', q5.risk_weight = 8.0, q5.category = 'Cyber';
MERGE (q5)-[:BELONGS_TO]->(d)

MERGE (q6:AssessmentQuestion {id: 'CYB-06'})
  SET q6.text = 'Are AI model endpoints and training infrastructure monitored for anomalies and threats? (CIS8-8)',
      q6.domain = 'Cyber Security', q6.risk_weight = 7.0, q6.category = 'Cyber';
MERGE (q6)-[:BELONGS_TO]->(d)

MERGE (q7:AssessmentQuestion {id: 'CYB-07'})
  SET q7.text = 'Is there a vulnerability management process covering AI libraries, dependencies and model weights? (CIS8-7)',
      q7.domain = 'Cyber Security', q7.risk_weight = 7.0, q7.category = 'Cyber';
MERGE (q7)-[:BELONGS_TO]->(d)

MERGE (q8:AssessmentQuestion {id: 'CYB-08'})
  SET q8.text = 'Are audit logs retained for AI system actions and access for at least 12 months? (CIS8-8)',
      q8.domain = 'Cyber Security', q8.risk_weight = 7.0, q8.category = 'Cyber';
MERGE (q8)-[:BELONGS_TO]->(d)

MERGE (q9:AssessmentQuestion {id: 'CYB-09'})
  SET q9.text = 'Has an incident response plan been defined specifically for AI model compromise or data poisoning? (CIS8-17)',
      q9.domain = 'Cyber Security', q9.risk_weight = 8.0, q9.category = 'Cyber';
MERGE (q9)-[:BELONGS_TO]->(d)

MERGE (q10:AssessmentQuestion {id: 'CYB-10'})
  SET q10.text = 'Is penetration testing or red-team adversarial testing planned for the AI system? (CIS8-18)',
      q10.domain = 'Cyber Security', q10.risk_weight = 7.0, q10.category = 'Cyber';
MERGE (q10)-[:BELONGS_TO]->(d)

MERGE (q11:AssessmentQuestion {id: 'CYB-11'})
  SET q11.text = 'Are AI training datasets protected from tampering or poisoning attacks? (CIS8-3)',
      q11.domain = 'Cyber Security', q11.risk_weight = 9.0, q11.category = 'Cyber';
MERGE (q11)-[:BELONGS_TO]->(d)

MERGE (q12:AssessmentQuestion {id: 'CYB-12'})
  SET q12.text = 'Is network access to AI inference endpoints segmented and firewall-controlled? (CIS8-12)',
      q12.domain = 'Cyber Security', q12.risk_weight = 7.0, q12.category = 'Cyber';
MERGE (q12)-[:BELONGS_TO]->(d)
