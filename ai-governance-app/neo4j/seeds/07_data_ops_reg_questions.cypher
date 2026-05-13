// ── Data Governance, Operational Risk & Regulatory Questions ─────────────────
MATCH (d_dat:RiskDomain {id: 'RD-DAT'})
MATCH (d_ops:RiskDomain {id: 'RD-OPS'})
MATCH (d_reg:RiskDomain {id: 'RD-REG'})

// Data Governance
MERGE (q1:AssessmentQuestion {id: 'DAT-01'})
  SET q1.text = 'Are all data sources for training and inference catalogued with data classification labels?',
      q1.domain = 'Data Governance', q1.risk_weight = 7.0, q1.category = 'Data';
MERGE (q1)-[:BELONGS_TO]->(d_dat)

MERGE (q2:AssessmentQuestion {id: 'DAT-02'})
  SET q2.text = 'Is there a data quality framework ensuring training data is accurate, complete, and representative?',
      q2.domain = 'Data Governance', q2.risk_weight = 8.0, q2.category = 'Data';
MERGE (q2)-[:BELONGS_TO]->(d_dat)

MERGE (q3:AssessmentQuestion {id: 'DAT-03'})
  SET q3.text = 'Are data lineage and citations traceable from AI outputs back to source documents?',
      q3.domain = 'Data Governance', q3.risk_weight = 7.0, q3.category = 'Data';
MERGE (q3)-[:BELONGS_TO]->(d_dat)

MERGE (q4:AssessmentQuestion {id: 'DAT-04'})
  SET q4.text = 'Is there a data access control policy limiting who can read/write AI training and inference data?',
      q4.domain = 'Data Governance', q4.risk_weight = 7.0, q4.category = 'Data';
MERGE (q4)-[:BELONGS_TO]->(d_dat)

MERGE (q5:AssessmentQuestion {id: 'DAT-05'})
  SET q5.text = 'Are DMOs (Data Model Objects) or schemas approved by the data governance team?',
      q5.domain = 'Data Governance', q5.risk_weight = 6.0, q5.category = 'Data';
MERGE (q5)-[:BELONGS_TO]->(d_dat)

// Operational Risk
MERGE (q6:AssessmentQuestion {id: 'OPS-01'})
  SET q6.text = 'Is there a disaster recovery plan for AI services including RTO and RPO targets?',
      q6.domain = 'Operational Risk', q6.risk_weight = 7.0, q6.category = 'Operations';
MERGE (q6)-[:BELONGS_TO]->(d_ops)

MERGE (q7:AssessmentQuestion {id: 'OPS-02'})
  SET q7.text = 'Are observability and monitoring dashboards in place for AI model performance and errors?',
      q7.domain = 'Operational Risk', q7.risk_weight = 7.0, q7.category = 'Operations';
MERGE (q7)-[:BELONGS_TO]->(d_ops)

MERGE (q8:AssessmentQuestion {id: 'OPS-03'})
  SET q8.text = 'Is there a change management process for updating AI models in production?',
      q8.domain = 'Operational Risk', q8.risk_weight = 7.0, q8.category = 'Operations';
MERGE (q8)-[:BELONGS_TO]->(d_ops)

MERGE (q9:AssessmentQuestion {id: 'OPS-04'})
  SET q9.text = 'Is the AI system architecture loosely coupled with defined API contracts to avoid tight dependencies?',
      q9.domain = 'Operational Risk', q9.risk_weight = 6.0, q9.category = 'Operations';
MERGE (q9)-[:BELONGS_TO]->(d_ops)

MERGE (q10:AssessmentQuestion {id: 'OPS-05'})
  SET q10.text = 'Is there a support and incident management runbook for AI-related incidents?',
      q10.domain = 'Operational Risk', q10.risk_weight = 7.0, q10.category = 'Operations';
MERGE (q10)-[:BELONGS_TO]->(d_ops)

// Regulatory & Legal
MERGE (q11:AssessmentQuestion {id: 'REG-01'})
  SET q11.text = 'Has the project been assessed against EU AI Act risk classification requirements?',
      q11.domain = 'Regulatory & Legal', q11.risk_weight = 9.0, q11.category = 'Regulatory';
MERGE (q11)-[:BELONGS_TO]->(d_reg)

MERGE (q12:AssessmentQuestion {id: 'REG-02'})
  SET q12.text = 'Is the AI system compliant with ISO 42001 AI Management System requirements?',
      q12.domain = 'Regulatory & Legal', q12.risk_weight = 8.0, q12.category = 'Regulatory';
MERGE (q12)-[:BELONGS_TO]->(d_reg)

MERGE (q13:AssessmentQuestion {id: 'REG-03'})
  SET q13.text = 'Are NIST AI RMF GOVERN, MAP, MEASURE and MANAGE functions addressed in the project plan?',
      q13.domain = 'Regulatory & Legal', q13.risk_weight = 8.0, q13.category = 'Regulatory';
MERGE (q13)-[:BELONGS_TO]->(d_reg)

MERGE (q14:AssessmentQuestion {id: 'REG-04'})
  SET q14.text = 'Has legal reviewed the AI system for compliance with Australian Privacy Act 1988 and APP requirements?',
      q14.domain = 'Regulatory & Legal', q14.risk_weight = 9.0, q14.category = 'Regulatory';
MERGE (q14)-[:BELONGS_TO]->(d_reg)

MERGE (q15:AssessmentQuestion {id: 'REG-05'})
  SET q15.text = 'Are there mechanisms to provide individuals with explanations of automated AI decisions that affect them?',
      q15.domain = 'Regulatory & Legal', q15.risk_weight = 9.0, q15.category = 'Regulatory';
MERGE (q15)-[:BELONGS_TO]->(d_reg)
