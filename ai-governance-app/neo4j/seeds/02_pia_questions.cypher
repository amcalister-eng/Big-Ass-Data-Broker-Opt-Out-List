// ── PIA Assessment Questions ──────────────────────────────────────────────────
MATCH (d:RiskDomain {id: 'RD-PIA'})

MERGE (q1:AssessmentQuestion {id: 'PIA-01'})
  SET q1.text = 'Does the project collect, use or disclose personal information?',
      q1.domain = 'Privacy & PIA', q1.risk_weight = 8.0, q1.category = 'PIA';
MERGE (q1)-[:BELONGS_TO]->(d)

MERGE (q2:AssessmentQuestion {id: 'PIA-02'})
  SET q2.text = 'What is the primary purpose for collecting personal information and is it clearly documented?',
      q2.domain = 'Privacy & PIA', q2.risk_weight = 7.0, q2.category = 'PIA';
MERGE (q2)-[:BELONGS_TO]->(d)

MERGE (q3:AssessmentQuestion {id: 'PIA-03'})
  SET q3.text = 'Is personal information collected only to the extent necessary for the stated purpose (data minimisation)?',
      q3.domain = 'Privacy & PIA', q3.risk_weight = 7.0, q3.category = 'PIA';
MERGE (q3)-[:BELONGS_TO]->(d)

MERGE (q4:AssessmentQuestion {id: 'PIA-04'})
  SET q4.text = 'Are individuals notified at or before the time of collection about how their information will be used?',
      q4.domain = 'Privacy & PIA', q4.risk_weight = 8.0, q4.category = 'PIA';
MERGE (q4)-[:BELONGS_TO]->(d)

MERGE (q5:AssessmentQuestion {id: 'PIA-05'})
  SET q5.text = 'Does the project involve sensitive information (health, financial, biometric, racial/ethnic origin)?',
      q5.domain = 'Privacy & PIA', q5.risk_weight = 9.0, q5.category = 'PIA';
MERGE (q5)-[:BELONGS_TO]->(d)

MERGE (q6:AssessmentQuestion {id: 'PIA-06'})
  SET q6.text = 'Are individuals able to access and correct their personal information held by the system?',
      q6.domain = 'Privacy & PIA', q6.risk_weight = 7.0, q6.category = 'PIA';
MERGE (q6)-[:BELONGS_TO]->(d)

MERGE (q7:AssessmentQuestion {id: 'PIA-07'})
  SET q7.text = 'Is personal information disclosed to third parties, and if so, are appropriate agreements in place?',
      q7.domain = 'Privacy & PIA', q7.risk_weight = 8.0, q7.category = 'PIA';
MERGE (q7)-[:BELONGS_TO]->(d)

MERGE (q8:AssessmentQuestion {id: 'PIA-08'})
  SET q8.text = 'Is personal information transferred or stored outside of Australia, and are cross-border transfer requirements met?',
      q8.domain = 'Privacy & PIA', q8.risk_weight = 8.0, q8.category = 'PIA';
MERGE (q8)-[:BELONGS_TO]->(d)

MERGE (q9:AssessmentQuestion {id: 'PIA-09'})
  SET q9.text = 'What retention periods apply to personal information and is there a process for secure destruction?',
      q9.domain = 'Privacy & PIA', q9.risk_weight = 6.0, q9.category = 'PIA';
MERGE (q9)-[:BELONGS_TO]->(d)

MERGE (q10:AssessmentQuestion {id: 'PIA-10'})
  SET q10.text = 'Has a Privacy Impact Assessment (PIA) been completed or is one planned?',
      q10.domain = 'Privacy & PIA', q10.risk_weight = 9.0, q10.category = 'PIA';
MERGE (q10)-[:BELONGS_TO]->(d)

MERGE (q11:AssessmentQuestion {id: 'PIA-11'})
  SET q11.text = 'Does the AI system make automated decisions with legal or similarly significant effects on individuals?',
      q11.domain = 'Privacy & PIA', q11.risk_weight = 10.0, q11.category = 'PIA';
MERGE (q11)-[:BELONGS_TO]->(d)

MERGE (q12:AssessmentQuestion {id: 'PIA-12'})
  SET q12.text = 'Are there measures to protect against unsolicited marketing or use of information beyond the collected purpose?',
      q12.domain = 'Privacy & PIA', q12.risk_weight = 6.0, q12.category = 'PIA';
MERGE (q12)-[:BELONGS_TO]->(d)

MERGE (q13:AssessmentQuestion {id: 'PIA-13'})
  SET q13.text = 'Does the project involve profiling of individuals, and are individuals aware of this?',
      q13.domain = 'Privacy & PIA', q13.risk_weight = 8.0, q13.category = 'PIA';
MERGE (q13)-[:BELONGS_TO]->(d)

MERGE (q14:AssessmentQuestion {id: 'PIA-14'})
  SET q14.text = 'Are privacy risks documented and escalated appropriately (Privacy Risk Register)?',
      q14.domain = 'Privacy & PIA', q14.risk_weight = 7.0, q14.category = 'PIA';
MERGE (q14)-[:BELONGS_TO]->(d)

MERGE (q15:AssessmentQuestion {id: 'PIA-15'})
  SET q15.text = 'Has the Privacy team been consulted on the design of data flows and consent mechanisms?',
      q15.domain = 'Privacy & PIA', q15.risk_weight = 7.0, q15.category = 'PIA';
MERGE (q15)-[:BELONGS_TO]->(d)
