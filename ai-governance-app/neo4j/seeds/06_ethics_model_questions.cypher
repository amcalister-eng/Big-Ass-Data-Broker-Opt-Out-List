// ── Ethics, Fairness & Model Risk Questions ───────────────────────────────────
MATCH (d_eth:RiskDomain {id: 'RD-ETH'})
MATCH (d_mdl:RiskDomain {id: 'RD-MDL'})

// Ethics & Fairness
MERGE (q1:AssessmentQuestion {id: 'ETH-01'})
  SET q1.text = 'Has a bias and fairness analysis been conducted for the training data and model outputs?',
      q1.domain = 'Ethics & Fairness', q1.risk_weight = 9.0, q1.category = 'Ethics';
MERGE (q1)-[:BELONGS_TO]->(d_eth)

MERGE (q2:AssessmentQuestion {id: 'ETH-02'})
  SET q2.text = 'Does the AI system treat protected cohorts (age, gender, race, disability) equitably?',
      q2.domain = 'Ethics & Fairness', q2.risk_weight = 9.0, q2.category = 'Ethics';
MERGE (q2)-[:BELONGS_TO]->(d_eth)

MERGE (q3:AssessmentQuestion {id: 'ETH-03'})
  SET q3.text = 'Can the AI system explain its decisions in human-understandable terms (explainability)?',
      q3.domain = 'Ethics & Fairness', q3.risk_weight = 8.0, q3.category = 'Ethics';
MERGE (q3)-[:BELONGS_TO]->(d_eth)

MERGE (q4:AssessmentQuestion {id: 'ETH-04'})
  SET q4.text = 'Is there a documented ethics review or RAI (Responsible AI) assessment for this project?',
      q4.domain = 'Ethics & Fairness', q4.risk_weight = 8.0, q4.category = 'Ethics';
MERGE (q4)-[:BELONGS_TO]->(d_eth)

MERGE (q5:AssessmentQuestion {id: 'ETH-05'})
  SET q5.text = 'Are there mechanisms to detect and remediate bias introduced by the AI system over time?',
      q5.domain = 'Ethics & Fairness', q5.risk_weight = 8.0, q5.category = 'Ethics';
MERGE (q5)-[:BELONGS_TO]->(d_eth)

MERGE (q6:AssessmentQuestion {id: 'ETH-06'})
  SET q6.text = 'Is there a clear RACI for AI ethics accountability including an identified AI ethics owner?',
      q6.domain = 'Ethics & Fairness', q6.risk_weight = 7.0, q6.category = 'Ethics';
MERGE (q6)-[:BELONGS_TO]->(d_eth)

MERGE (q7:AssessmentQuestion {id: 'ETH-07'})
  SET q7.text = 'Are quantifiable success metrics (KPIs) defined for fairness and responsible AI performance?',
      q7.domain = 'Ethics & Fairness', q7.risk_weight = 6.0, q7.category = 'Ethics';
MERGE (q7)-[:BELONGS_TO]->(d_eth)

// Model Risk
MERGE (q8:AssessmentQuestion {id: 'MDL-01'})
  SET q8.text = 'Is a model card or equivalent documentation available for all AI models used in the project?',
      q8.domain = 'Model Risk', q8.risk_weight = 7.0, q8.category = 'ModelRisk';
MERGE (q8)-[:BELONGS_TO]->(d_mdl)

MERGE (q9:AssessmentQuestion {id: 'MDL-02'})
  SET q9.text = 'Has the model been validated against an independent test dataset before production deployment?',
      q9.domain = 'Model Risk', q9.risk_weight = 8.0, q9.category = 'ModelRisk';
MERGE (q9)-[:BELONGS_TO]->(d_mdl)

MERGE (q10:AssessmentQuestion {id: 'MDL-03'})
  SET q10.text = 'Is model drift monitored post-deployment with defined thresholds for retraining or rollback?',
      q10.domain = 'Model Risk', q10.risk_weight = 8.0, q10.category = 'ModelRisk';
MERGE (q10)-[:BELONGS_TO]->(d_mdl)

MERGE (q11:AssessmentQuestion {id: 'MDL-04'})
  SET q11.text = 'Are hallucination rates and confidence calibration assessed for generative AI models?',
      q11.domain = 'Model Risk', q11.risk_weight = 8.0, q11.category = 'ModelRisk';
MERGE (q11)-[:BELONGS_TO]->(d_mdl)

MERGE (q12:AssessmentQuestion {id: 'MDL-05'})
  SET q12.text = 'Is there a rollback or model versioning strategy if a deployed model performs below acceptable thresholds?',
      q12.domain = 'Model Risk', q12.risk_weight = 7.0, q12.category = 'ModelRisk';
MERGE (q12)-[:BELONGS_TO]->(d_mdl)

MERGE (q13:AssessmentQuestion {id: 'MDL-06'})
  SET q13.text = 'Are training data lineage and provenance documented and auditable?',
      q13.domain = 'Model Risk', q13.risk_weight = 7.0, q13.category = 'ModelRisk';
MERGE (q13)-[:BELONGS_TO]->(d_mdl)
