// ── ARB / Agentic Review Board Questions (questions only, not template responses) ──
MATCH (d:RiskDomain {id: 'RD-ARB'})

// 1. Business Alignment & Strategy
MERGE (q1:AssessmentQuestion {id: 'ARB-01'})
  SET q1.text = 'Does the agent solve a clearly defined business problem, and has the business justification been documented?',
      q1.domain = 'ARB / Agentic Review', q1.risk_weight = 7.0, q1.category = 'ARB-Business';
MERGE (q1)-[:BELONGS_TO]->(d)

MERGE (q2:AssessmentQuestion {id: 'ARB-02'})
  SET q2.text = 'Have existing agents, AI assets, or approved models been assessed for reuse before building new?',
      q2.domain = 'ARB / Agentic Review', q2.risk_weight = 5.0, q2.category = 'ARB-Business';
MERGE (q2)-[:BELONGS_TO]->(d)

MERGE (q3:AssessmentQuestion {id: 'ARB-03'})
  SET q3.text = 'Are quantifiable success metrics (KPIs) defined, such as response time reduction or task automation rate?',
      q3.domain = 'ARB / Agentic Review', q3.risk_weight = 6.0, q3.category = 'ARB-Business';
MERGE (q3)-[:BELONGS_TO]->(d)

MERGE (q4:AssessmentQuestion {id: 'ARB-04'})
  SET q4.text = 'Is a clear RACI matrix defined for agent ownership, and is an incident management plan in place?',
      q4.domain = 'ARB / Agentic Review', q4.risk_weight = 7.0, q4.category = 'ARB-Business';
MERGE (q4)-[:BELONGS_TO]->(d)

// 2. Data Architecture & Governance
MERGE (q5:AssessmentQuestion {id: 'ARB-05'})
  SET q5.text = 'Have all Data Cloud DMOs and Salesforce Objects used by the agent been approved by the data governance team?',
      q5.domain = 'ARB / Agentic Review', q5.risk_weight = 7.0, q5.category = 'ARB-Data';
MERGE (q5)-[:BELONGS_TO]->(d)

MERGE (q6:AssessmentQuestion {id: 'ARB-06'})
  SET q6.text = 'Is the principle of least privilege applied to agent access via Permission Sets and Sharing Rules?',
      q6.domain = 'ARB / Agentic Review', q6.risk_weight = 8.0, q6.category = 'ARB-Data';
MERGE (q6)-[:BELONGS_TO]->(d)

MERGE (q7:AssessmentQuestion {id: 'ARB-07'})
  SET q7.text = 'Is the Einstein Trust Layer (or equivalent) used for PII/PCI masking, toxicity detection, and zero data retention?',
      q7.domain = 'ARB / Agentic Review', q7.risk_weight = 9.0, q7.category = 'ARB-Data';
MERGE (q7)-[:BELONGS_TO]->(d)

MERGE (q8:AssessmentQuestion {id: 'ARB-08'})
  SET q8.text = 'Can answers provided by the agent be traced back to source documents via data lineage or citations?',
      q8.domain = 'ARB / Agentic Review', q8.risk_weight = 7.0, q8.category = 'ARB-Data';
MERGE (q8)-[:BELONGS_TO]->(d)

// 3. Knowledge & RAG Architecture
MERGE (q9:AssessmentQuestion {id: 'ARB-09'})
  SET q9.text = 'Are specific Data Categories and Article Types defined to scope the knowledge base for RAG retrieval?',
      q9.domain = 'ARB / Agentic Review', q9.risk_weight = 6.0, q9.category = 'ARB-RAG';
MERGE (q9)-[:BELONGS_TO]->(d)

MERGE (q10:AssessmentQuestion {id: 'ARB-10'})
  SET q10.text = 'Has retrieval quality been tested (e.g., via Agentforce Builder Conversation Preview or Testing Center)?',
      q10.domain = 'ARB / Agentic Review', q10.risk_weight = 7.0, q10.category = 'ARB-RAG';
MERGE (q10)-[:BELONGS_TO]->(d)

MERGE (q11:AssessmentQuestion {id: 'ARB-11'})
  SET q11.text = 'Is there a conflict resolution strategy for contradicting knowledge sources (prioritisation, upvoting)?',
      q11.domain = 'ARB / Agentic Review', q11.risk_weight = 6.0, q11.category = 'ARB-RAG';
MERGE (q11)-[:BELONGS_TO]->(d)

// 4. Security & Risk
MERGE (q12:AssessmentQuestion {id: 'ARB-12'})
  SET q12.text = 'Have threat surface mitigations been applied via the Salesforce Shared Responsibility Model and Salesforce Shield?',
      q12.domain = 'ARB / Agentic Review', q12.risk_weight = 8.0, q12.category = 'ARB-Security';
MERGE (q12)-[:BELONGS_TO]->(d)

MERGE (q13:AssessmentQuestion {id: 'ARB-13'})
  SET q13.text = 'Are prompt injection defences implemented including Toxicity Scoring and Injection Detection?',
      q13.domain = 'ARB / Agentic Review', q13.risk_weight = 9.0, q13.category = 'ARB-Security';
MERGE (q13)-[:BELONGS_TO]->(d)

MERGE (q14:AssessmentQuestion {id: 'ARB-14'})
  SET q14.text = 'Are all secrets managed via Named Credentials and OAuth 2.0 with no secrets stored in agent code?',
      q14.domain = 'ARB / Agentic Review', q14.risk_weight = 9.0, q14.category = 'ARB-Security';
MERGE (q14)-[:BELONGS_TO]->(d)

// 5. UX & Operational Readiness
MERGE (q15:AssessmentQuestion {id: 'ARB-15'})
  SET q15.text = 'Is there an escalation path (Omni-Channel routing or Web-to-Case fallback) when the agent cannot resolve a query?',
      q15.domain = 'ARB / Agentic Review', q15.risk_weight = 7.0, q15.category = 'ARB-UX';
MERGE (q15)-[:BELONGS_TO]->(d)

MERGE (q16:AssessmentQuestion {id: 'ARB-16'})
  SET q16.text = 'Are Reasoning Engine Traces available and are AI-generated response disclaimers shown to users?',
      q16.domain = 'ARB / Agentic Review', q16.risk_weight = 7.0, q16.category = 'ARB-UX';
MERGE (q16)-[:BELONGS_TO]->(d)

MERGE (q17:AssessmentQuestion {id: 'ARB-17'})
  SET q17.text = 'Is there a defined review cadence for the agent based on Digital Wallet flex credit consumption and usage reports?',
      q17.domain = 'ARB / Agentic Review', q17.risk_weight = 5.0, q17.category = 'ARB-UX';
MERGE (q17)-[:BELONGS_TO]->(d)

// 6. Resource & Cost
MERGE (q18:AssessmentQuestion {id: 'ARB-18'})
  SET q18.text = 'Have annual Flex Credit / compute costs been estimated with a monitoring plan via Digital Wallet?',
      q18.domain = 'ARB / Agentic Review', q18.risk_weight = 5.0, q18.category = 'ARB-Cost';
MERGE (q18)-[:BELONGS_TO]->(d)

MERGE (q19:AssessmentQuestion {id: 'ARB-19'})
  SET q19.text = 'If custom development (Apex) was used, has the justification been documented explaining why no-code tools were insufficient?',
      q19.domain = 'ARB / Agentic Review', q19.risk_weight = 5.0, q19.category = 'ARB-Cost';
MERGE (q19)-[:BELONGS_TO]->(d)

// ARB Document Metadata
MERGE (q20:AssessmentQuestion {id: 'ARB-20'})
  SET q20.text = 'Has the design been socialised with key stakeholders prior to ARB review?',
      q20.domain = 'ARB / Agentic Review', q20.risk_weight = 6.0, q20.category = 'ARB-Process';
MERGE (q20)-[:BELONGS_TO]->(d)

MERGE (q21:AssessmentQuestion {id: 'ARB-21'})
  SET q21.text = 'Has a peer review been conducted by a Technical Lead or Architect with relevant GenAI/Agentic experience?',
      q21.domain = 'ARB / Agentic Review', q21.risk_weight = 6.0, q21.category = 'ARB-Process';
MERGE (q21)-[:BELONGS_TO]->(d)

MERGE (q22:AssessmentQuestion {id: 'ARB-22'})
  SET q22.text = 'What is the primary agentic paradigm (Single-Agent, Multi-Agent Orchestration, or specialised type) and is it documented?',
      q22.domain = 'ARB / Agentic Review', q22.risk_weight = 7.0, q22.category = 'ARB-Process';
MERGE (q22)-[:BELONGS_TO]->(d)
