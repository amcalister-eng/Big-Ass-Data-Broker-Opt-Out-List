"""Seed all governance data into SQLite."""
from app.core.database_sqlite import get_conn, init_db

DOMAINS = [
    ("RD-PIA",  "Privacy & PIA",          "#8b5cf6", 1),
    ("RD-SUP",  "Supplier & Third Party",  "#06b6d4", 2),
    ("RD-AGT",  "Agentic AI",              "#f59e0b", 3),
    ("RD-CYB",  "Cyber Security",          "#ef4444", 4),
    ("RD-ETH",  "Ethics & Fairness",       "#ec4899", 5),
    ("RD-DAT",  "Data Governance",         "#10b981", 6),
    ("RD-MDL",  "Model Risk",              "#6366f1", 7),
    ("RD-OPS",  "Operational Risk",        "#84cc16", 8),
    ("RD-REG",  "Regulatory & Legal",      "#f97316", 9),
    ("RD-ARB",  "ARB / Agentic Review",    "#14b8a6", 10),
]

QUESTIONS = [
    # PIA
    ("PIA-01","Does the project collect, use or disclose personal information?","Privacy & PIA",8.0,"PIA","RD-PIA"),
    ("PIA-02","What is the primary purpose for collecting personal information and is it clearly documented?","Privacy & PIA",7.0,"PIA","RD-PIA"),
    ("PIA-03","Is personal information collected only to the extent necessary for the stated purpose (data minimisation)?","Privacy & PIA",7.0,"PIA","RD-PIA"),
    ("PIA-04","Are individuals notified at or before the time of collection about how their information will be used?","Privacy & PIA",8.0,"PIA","RD-PIA"),
    ("PIA-05","Does the project involve sensitive information (health, financial, biometric, racial/ethnic origin)?","Privacy & PIA",9.0,"PIA","RD-PIA"),
    ("PIA-06","Are individuals able to access and correct their personal information held by the system?","Privacy & PIA",7.0,"PIA","RD-PIA"),
    ("PIA-07","Is personal information disclosed to third parties, and if so, are appropriate agreements in place?","Privacy & PIA",8.0,"PIA","RD-PIA"),
    ("PIA-08","Is personal information transferred or stored outside of Australia?","Privacy & PIA",8.0,"PIA","RD-PIA"),
    ("PIA-09","What retention periods apply to personal information and is there a process for secure destruction?","Privacy & PIA",6.0,"PIA","RD-PIA"),
    ("PIA-10","Has a Privacy Impact Assessment (PIA) been completed or is one planned?","Privacy & PIA",9.0,"PIA","RD-PIA"),
    ("PIA-11","Does the AI system make automated decisions with legal or similarly significant effects on individuals?","Privacy & PIA",10.0,"PIA","RD-PIA"),
    ("PIA-12","Are there measures to protect against use of information beyond the collected purpose?","Privacy & PIA",6.0,"PIA","RD-PIA"),
    ("PIA-13","Does the project involve profiling of individuals, and are individuals aware of this?","Privacy & PIA",8.0,"PIA","RD-PIA"),
    ("PIA-14","Are privacy risks documented and escalated appropriately (Privacy Risk Register)?","Privacy & PIA",7.0,"PIA","RD-PIA"),
    ("PIA-15","Has the Privacy team been consulted on data flows and consent mechanisms?","Privacy & PIA",7.0,"PIA","RD-PIA"),
    # Supplier
    ("SUP-01","Has a Supplier Risk Assessment been completed for all AI vendors and model providers?","Supplier & Third Party",8.0,"Supplier","RD-SUP"),
    ("SUP-02","Are data processing agreements (DPAs) or AI-specific addenda in place with all AI suppliers?","Supplier & Third Party",8.0,"Supplier","RD-SUP"),
    ("SUP-03","Does the supplier retain training rights over data submitted to their models?","Supplier & Third Party",9.0,"Supplier","RD-SUP"),
    ("SUP-04","Are model cards available for all third-party AI models used?","Supplier & Third Party",6.0,"Supplier","RD-SUP"),
    ("SUP-05","Is there a process to monitor AI supplier performance, drift, and responsible AI compliance?","Supplier & Third Party",7.0,"Supplier","RD-SUP"),
    ("SUP-06","Does the supplier have an established responsible/ethical AI policy?","Supplier & Third Party",7.0,"Supplier","RD-SUP"),
    ("SUP-07","Is there a documented exit/transition plan if the AI supplier is replaced?","Supplier & Third Party",6.0,"Supplier","RD-SUP"),
    ("SUP-08","Has IP ownership of AI outputs been clarified with legal and the supplier contract?","Supplier & Third Party",7.0,"Supplier","RD-SUP"),
    ("SUP-09","Are fourth-party risks (sub-processors used by the AI vendor) assessed?","Supplier & Third Party",6.0,"Supplier","RD-SUP"),
    ("SUP-10","Is the AI supplier subject to regular security audits (SOC 2, ISO 27001)?","Supplier & Third Party",7.0,"Supplier","RD-SUP"),
    # Agentic
    ("AGT-01","What is the autonomy level of the agent (human-in-the-loop, supervised, or fully autonomous)?","Agentic AI",10.0,"Agentic","RD-AGT"),
    ("AGT-02","Are there defined boundaries on the tools, actions and data the agent can access?","Agentic AI",9.0,"Agentic","RD-AGT"),
    ("AGT-03","Is there a human escalation and override mechanism for high-risk agent decisions?","Agentic AI",10.0,"Agentic","RD-AGT"),
    ("AGT-04","Is the agentic framework (single-agent vs multi-agent) documented and justified?","Agentic AI",7.0,"Agentic","RD-AGT"),
    ("AGT-05","Are the core LLMs routed through an approved trust layer?","Agentic AI",8.0,"Agentic","RD-AGT"),
    ("AGT-06","Are prompt injection and adversarial attack mitigations implemented?","Agentic AI",9.0,"Agentic","RD-AGT"),
    ("AGT-07","Are agent reasoning traces logged and auditable?","Agentic AI",8.0,"Agentic","RD-AGT"),
    ("AGT-08","Are Flex Credit / compute costs estimated and monitored?","Agentic AI",5.0,"Agentic","RD-AGT"),
    ("AGT-09","Is there a fallback/escalation path if the agent fails or produces an uncertain result?","Agentic AI",8.0,"Agentic","RD-AGT"),
    ("AGT-10","Has the Agentic AI COE reviewed the agent design prior to development?","Agentic AI",8.0,"Agentic","RD-AGT"),
    ("AGT-11","Are secrets (API keys, credentials) managed via a secrets manager?","Agentic AI",9.0,"Agentic","RD-AGT"),
    ("AGT-12","Is the agent subject to a review cadence after deployment?","Agentic AI",6.0,"Agentic","RD-AGT"),
    ("AGT-13","Is there an AI-generated response disclaimer presented to users?","Agentic AI",7.0,"Agentic","RD-AGT"),
    ("AGT-14","Are toxicity detection and PII/PCI masking applied to agent inputs and outputs?","Agentic AI",8.0,"Agentic","RD-AGT"),
    ("AGT-15","Can existing agents or approved assets be reused rather than building new?","Agentic AI",4.0,"Agentic","RD-AGT"),
    # Cyber
    ("CYB-01","Is an inventory of assets that process AI model data maintained? (CIS8-1/2)","Cyber Security",6.0,"Cyber","RD-CYB"),
    ("CYB-02","Are data flows for AI inputs/outputs documented and classified? (CIS8-3)","Cyber Security",7.0,"Cyber","RD-CYB"),
    ("CYB-03","Are accounts accessing AI infrastructure protected with MFA and least-privilege? (CIS8-5/6)","Cyber Security",8.0,"Cyber","RD-CYB"),
    ("CYB-04","Is data used for AI training/inference encrypted at rest and in transit? (CIS8-3)","Cyber Security",8.0,"Cyber","RD-CYB"),
    ("CYB-05","Is API access to AI models secured with key management and rate limiting? (CIS8-4)","Cyber Security",8.0,"Cyber","RD-CYB"),
    ("CYB-06","Are AI model endpoints monitored for anomalies and threats? (CIS8-8)","Cyber Security",7.0,"Cyber","RD-CYB"),
    ("CYB-07","Is there a vulnerability management process covering AI libraries and dependencies? (CIS8-7)","Cyber Security",7.0,"Cyber","RD-CYB"),
    ("CYB-08","Are audit logs retained for AI system actions for at least 12 months? (CIS8-8)","Cyber Security",7.0,"Cyber","RD-CYB"),
    ("CYB-09","Has an incident response plan been defined for AI model compromise? (CIS8-17)","Cyber Security",8.0,"Cyber","RD-CYB"),
    ("CYB-10","Is penetration testing or red-team adversarial testing planned? (CIS8-18)","Cyber Security",7.0,"Cyber","RD-CYB"),
    ("CYB-11","Are AI training datasets protected from tampering or poisoning? (CIS8-3)","Cyber Security",9.0,"Cyber","RD-CYB"),
    ("CYB-12","Is network access to AI inference endpoints segmented and firewall-controlled? (CIS8-12)","Cyber Security",7.0,"Cyber","RD-CYB"),
    # Ethics
    ("ETH-01","Has a bias and fairness analysis been conducted for the training data and model outputs?","Ethics & Fairness",9.0,"Ethics","RD-ETH"),
    ("ETH-02","Does the AI system treat protected cohorts equitably?","Ethics & Fairness",9.0,"Ethics","RD-ETH"),
    ("ETH-03","Can the AI system explain its decisions in human-understandable terms?","Ethics & Fairness",8.0,"Ethics","RD-ETH"),
    ("ETH-04","Is there a documented ethics review or RAI assessment for this project?","Ethics & Fairness",8.0,"Ethics","RD-ETH"),
    ("ETH-05","Are there mechanisms to detect and remediate bias over time?","Ethics & Fairness",8.0,"Ethics","RD-ETH"),
    ("ETH-06","Is there a clear RACI for AI ethics accountability?","Ethics & Fairness",7.0,"Ethics","RD-ETH"),
    ("ETH-07","Are quantifiable KPIs defined for fairness and responsible AI performance?","Ethics & Fairness",6.0,"Ethics","RD-ETH"),
    # Model Risk
    ("MDL-01","Is a model card available for all AI models used in the project?","Model Risk",7.0,"ModelRisk","RD-MDL"),
    ("MDL-02","Has the model been validated against an independent test dataset before production?","Model Risk",8.0,"ModelRisk","RD-MDL"),
    ("MDL-03","Is model drift monitored post-deployment with defined thresholds for retraining?","Model Risk",8.0,"ModelRisk","RD-MDL"),
    ("MDL-04","Are hallucination rates and confidence calibration assessed for generative AI models?","Model Risk",8.0,"ModelRisk","RD-MDL"),
    ("MDL-05","Is there a rollback or model versioning strategy?","Model Risk",7.0,"ModelRisk","RD-MDL"),
    ("MDL-06","Are training data lineage and provenance documented and auditable?","Model Risk",7.0,"ModelRisk","RD-MDL"),
    # Data
    ("DAT-01","Are all data sources catalogued with data classification labels?","Data Governance",7.0,"Data","RD-DAT"),
    ("DAT-02","Is there a data quality framework ensuring training data is accurate and representative?","Data Governance",8.0,"Data","RD-DAT"),
    ("DAT-03","Are data lineage and citations traceable from AI outputs back to source documents?","Data Governance",7.0,"Data","RD-DAT"),
    ("DAT-04","Is there a data access control policy for AI training and inference data?","Data Governance",7.0,"Data","RD-DAT"),
    ("DAT-05","Are DMOs or schemas approved by the data governance team?","Data Governance",6.0,"Data","RD-DAT"),
    # Ops
    ("OPS-01","Is there a disaster recovery plan for AI services including RTO and RPO targets?","Operational Risk",7.0,"Operations","RD-OPS"),
    ("OPS-02","Are observability and monitoring dashboards in place for AI model performance?","Operational Risk",7.0,"Operations","RD-OPS"),
    ("OPS-03","Is there a change management process for updating AI models in production?","Operational Risk",7.0,"Operations","RD-OPS"),
    ("OPS-04","Is the AI system architecture loosely coupled with defined API contracts?","Operational Risk",6.0,"Operations","RD-OPS"),
    ("OPS-05","Is there a support and incident management runbook for AI-related incidents?","Operational Risk",7.0,"Operations","RD-OPS"),
    # Regulatory
    ("REG-01","Has the project been assessed against EU AI Act risk classification requirements?","Regulatory & Legal",9.0,"Regulatory","RD-REG"),
    ("REG-02","Is the AI system compliant with ISO 42001 AI Management System requirements?","Regulatory & Legal",8.0,"Regulatory","RD-REG"),
    ("REG-03","Are NIST AI RMF GOVERN, MAP, MEASURE and MANAGE functions addressed?","Regulatory & Legal",8.0,"Regulatory","RD-REG"),
    ("REG-04","Has legal reviewed the AI system for Australian Privacy Act 1988 compliance?","Regulatory & Legal",9.0,"Regulatory","RD-REG"),
    ("REG-05","Are there mechanisms to provide individuals with explanations of automated decisions?","Regulatory & Legal",9.0,"Regulatory","RD-REG"),
    # ARB
    ("ARB-01","Does the agent solve a clearly defined business problem with documented justification?","ARB / Agentic Review",7.0,"ARB-Business","RD-ARB"),
    ("ARB-02","Have existing agents or approved models been assessed for reuse before building new?","ARB / Agentic Review",5.0,"ARB-Business","RD-ARB"),
    ("ARB-03","Are quantifiable success metrics (KPIs) defined?","ARB / Agentic Review",6.0,"ARB-Business","RD-ARB"),
    ("ARB-04","Is a clear RACI matrix defined for agent ownership with an incident management plan?","ARB / Agentic Review",7.0,"ARB-Business","RD-ARB"),
    ("ARB-05","Have all Data Cloud DMOs used by the agent been approved by the data governance team?","ARB / Agentic Review",7.0,"ARB-Data","RD-ARB"),
    ("ARB-06","Is the principle of least privilege applied to agent access via Permission Sets?","ARB / Agentic Review",8.0,"ARB-Data","RD-ARB"),
    ("ARB-07","Is the Einstein Trust Layer (or equivalent) used for PII/PCI masking and toxicity detection?","ARB / Agentic Review",9.0,"ARB-Data","RD-ARB"),
    ("ARB-08","Can agent answers be traced back to source documents via data lineage?","ARB / Agentic Review",7.0,"ARB-Data","RD-ARB"),
    ("ARB-09","Are specific Data Categories and Article Types defined to scope RAG retrieval?","ARB / Agentic Review",6.0,"ARB-RAG","RD-ARB"),
    ("ARB-10","Has retrieval quality been tested via Conversation Preview or Testing Center?","ARB / Agentic Review",7.0,"ARB-RAG","RD-ARB"),
    ("ARB-11","Is there a conflict resolution strategy for contradicting knowledge sources?","ARB / Agentic Review",6.0,"ARB-RAG","RD-ARB"),
    ("ARB-12","Have threat surface mitigations been applied via Salesforce Shared Responsibility Model?","ARB / Agentic Review",8.0,"ARB-Security","RD-ARB"),
    ("ARB-13","Are prompt injection defences implemented including Toxicity Scoring and Injection Detection?","ARB / Agentic Review",9.0,"ARB-Security","RD-ARB"),
    ("ARB-14","Are all secrets managed via Named Credentials and OAuth 2.0 with no secrets in code?","ARB / Agentic Review",9.0,"ARB-Security","RD-ARB"),
    ("ARB-15","Is there an escalation path (Omni-Channel or Web-to-Case) when the agent cannot resolve a query?","ARB / Agentic Review",7.0,"ARB-UX","RD-ARB"),
    ("ARB-16","Are Reasoning Engine Traces available and are AI response disclaimers shown to users?","ARB / Agentic Review",7.0,"ARB-UX","RD-ARB"),
    ("ARB-17","Is there a defined review cadence based on Digital Wallet flex credit consumption?","ARB / Agentic Review",5.0,"ARB-UX","RD-ARB"),
    ("ARB-18","Have annual Flex Credit costs been estimated with a monitoring plan?","ARB / Agentic Review",5.0,"ARB-Cost","RD-ARB"),
    ("ARB-19","If custom development (Apex) was used, has the justification been documented?","ARB / Agentic Review",5.0,"ARB-Cost","RD-ARB"),
    ("ARB-20","Has the design been socialised with key stakeholders prior to ARB review?","ARB / Agentic Review",6.0,"ARB-Process","RD-ARB"),
    ("ARB-21","Has a peer review been conducted by a Technical Lead with GenAI/Agentic experience?","ARB / Agentic Review",6.0,"ARB-Process","RD-ARB"),
    ("ARB-22","Is the primary agentic paradigm documented (Single-Agent, Multi-Agent, or specialised)?","ARB / Agentic Review",7.0,"ARB-Process","RD-ARB"),
]

CONTROLS = [
    ("CR-PIA-DPIA","Conduct a Data Protection / Privacy Impact Assessment using the approved PIA template","Privacy & PIA","medium","PIA-10"),
    ("CR-AGT-HITL","Implement human-in-the-loop review gates for all high-risk agent decisions","Agentic AI","high","AGT-03"),
    ("CR-CYB-MFA","Enforce MFA on all accounts with access to AI infrastructure","Cyber Security","low","CYB-03"),
    ("CR-MDL-CARD","Publish a model card for all AI models in the enterprise model registry","Model Risk","medium","MDL-01"),
    ("CR-ETH-BIAS","Run bias evaluation toolkit on training data and model predictions","Ethics & Fairness","high","ETH-01"),
    ("CR-SUP-DPA","Execute AI-specific data processing addendum with all LLM/AI suppliers before go-live","Supplier & Third Party","medium","SUP-02"),
]

PATTERNS = [
    ("GP-REGISTER","Register: Log AI system in AI Registry before development begins","Register",1,["ETH-04"]),
    ("GP-ASSESS","Assess: Complete PIA, RAI Scorecard, and Supplier Risk Assessment","Assess",2,["PIA-10"]),
    ("GP-REVIEW","Review: Submit to ARB / AI Council for design review at architecture gate","Review",3,["ARB-01"]),
    ("GP-ALIGN","Align: Ensure compliance with EU AI Act, ISO 42001, NIST AIRF, and APPs","Align",4,["REG-01"]),
    ("GP-OPERATE","Operate: Monitor model drift, bias, and performance post-deployment","Operate",5,["MDL-03"]),
]

STANDARDS = [
    ("EU-AI-ACT","EU AI Act","2024","EU"),
    ("ISO-42001","ISO 42001 AI Management System","2023","Global"),
    ("NIST-AIRF","NIST AI Risk Management Framework","1.0","Global"),
    ("CIS8","CIS Controls v8","8.0","Global"),
    ("AUS-PRIVACY","Australian Privacy Act / APPs","1988","Australia"),
]

CLAUSES = [
    ("EU-AIA-ART9","EU-AI-ACT","Risk management system","Article 9"),
    ("EU-AIA-ART10","EU-AI-ACT","Data and data governance","Article 10"),
    ("EU-AIA-ART13","EU-AI-ACT","Transparency and provision of information to users","Article 13"),
    ("EU-AIA-ART14","EU-AI-ACT","Human oversight","Article 14"),
    ("EU-AIA-ART15","EU-AI-ACT","Accuracy, robustness and cybersecurity","Article 15"),
    ("ISO42001-6","ISO-42001","Planning — AI risk and opportunity management","Clause 6"),
    ("ISO42001-8","ISO-42001","Operation — AI system development controls","Clause 8"),
    ("ISO42001-9","ISO-42001","Performance evaluation","Clause 9"),
    ("NIST-GOVERN","NIST-AIRF","GOVERN — Policies, processes, accountability","GOVERN"),
    ("NIST-MAP","NIST-AIRF","MAP — Context and risk categorisation","MAP"),
    ("NIST-MEASURE","NIST-AIRF","MEASURE — Analysis and monitoring","MEASURE"),
    ("NIST-MANAGE","NIST-AIRF","MANAGE — Risk response and recovery","MANAGE"),
]

QUESTION_STANDARDS = [
    ("PIA-11","EU-AIA-ART14"),("ETH-03","EU-AIA-ART13"),("MDL-03","EU-AIA-ART15"),
    ("DAT-02","EU-AIA-ART10"),("REG-01","EU-AIA-ART9"),("REG-02","ISO42001-8"),
    ("REG-03","NIST-GOVERN"),("MDL-02","NIST-MEASURE"),("AGT-03","EU-AIA-ART14"),
    ("ETH-01","NIST-MAP"),
]


def seed():
    init_db()
    conn = get_conn()
    conn.execute("DELETE FROM risk_domains")
    conn.execute("DELETE FROM questions")
    conn.execute("DELETE FROM standards")
    conn.execute("DELETE FROM standard_clauses")
    conn.execute("DELETE FROM question_standards")
    conn.execute("DELETE FROM control_recommendations")
    conn.execute("DELETE FROM question_controls")
    conn.execute("DELETE FROM governance_patterns")
    conn.execute("DELETE FROM question_patterns")

    conn.executemany("INSERT INTO risk_domains VALUES (?,?,?,?)", DOMAINS)
    conn.executemany("INSERT INTO questions VALUES (?,?,?,?,?,?)", QUESTIONS)
    conn.executemany("INSERT INTO standards VALUES (?,?,?,?)", STANDARDS)
    conn.executemany("INSERT INTO standard_clauses VALUES (?,?,?,?)", CLAUSES)
    conn.executemany("INSERT INTO question_standards VALUES (?,?)", QUESTION_STANDARDS)

    for ctrl_id, desc, domain, effort, q_id in CONTROLS:
        conn.execute("INSERT INTO control_recommendations VALUES (?,?,?,?)", (ctrl_id, desc, domain, effort))
        conn.execute("INSERT INTO question_controls VALUES (?,?)", (q_id, ctrl_id))

    for pat_id, name, phase, order, q_ids in PATTERNS:
        conn.execute("INSERT INTO governance_patterns VALUES (?,?,?,?)", (pat_id, name, phase, order))
        for qid in q_ids:
            conn.execute("INSERT INTO question_patterns VALUES (?,?)", (qid, pat_id))

    conn.commit()
    conn.close()
    print(f"Seeded {len(QUESTIONS)} questions across {len(DOMAINS)} domains.")


if __name__ == "__main__":
    seed()
