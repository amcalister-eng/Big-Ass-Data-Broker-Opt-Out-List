// ── Governance Standards ──────────────────────────────────────────────────────
MERGE (eu:GovernanceStandard {id: 'EU-AI-ACT'})
  SET eu.name = 'EU AI Act', eu.version = '2024', eu.jurisdiction = 'EU';

MERGE (iso:GovernanceStandard {id: 'ISO-42001'})
  SET iso.name = 'ISO 42001 AI Management System', iso.version = '2023', iso.jurisdiction = 'Global';

MERGE (nist:GovernanceStandard {id: 'NIST-AIRF'})
  SET nist.name = 'NIST AI Risk Management Framework', nist.version = '1.0', nist.jurisdiction = 'Global';

MERGE (cis:GovernanceStandard {id: 'CIS8'})
  SET cis.name = 'CIS Controls v8', cis.version = '8.0', cis.jurisdiction = 'Global';

MERGE (app:GovernanceStandard {id: 'AUS-PRIVACY'})
  SET app.name = 'Australian Privacy Act / APPs', app.version = '1988', app.jurisdiction = 'Australia';

// ── Key Standard Clauses ──────────────────────────────────────────────────────
// EU AI Act
MERGE (c1:StandardClause {id: 'EU-AIA-ART9'})
  SET c1.standard_id = 'EU-AI-ACT', c1.title = 'Risk management system', c1.article = 'Article 9';
MERGE (c1)-[:PART_OF]->(eu)

MERGE (c2:StandardClause {id: 'EU-AIA-ART10'})
  SET c2.standard_id = 'EU-AI-ACT', c2.title = 'Data and data governance', c2.article = 'Article 10';
MERGE (c2)-[:PART_OF]->(eu)

MERGE (c3:StandardClause {id: 'EU-AIA-ART13'})
  SET c3.standard_id = 'EU-AI-ACT', c3.title = 'Transparency and provision of information to users', c3.article = 'Article 13';
MERGE (c3)-[:PART_OF]->(eu)

MERGE (c4:StandardClause {id: 'EU-AIA-ART14'})
  SET c4.standard_id = 'EU-AI-ACT', c4.title = 'Human oversight', c4.article = 'Article 14';
MERGE (c4)-[:PART_OF]->(eu)

MERGE (c5:StandardClause {id: 'EU-AIA-ART15'})
  SET c5.standard_id = 'EU-AI-ACT', c5.title = 'Accuracy, robustness and cybersecurity', c5.article = 'Article 15';
MERGE (c5)-[:PART_OF]->(eu)

// ISO 42001
MERGE (i1:StandardClause {id: 'ISO42001-6'})
  SET i1.standard_id = 'ISO-42001', i1.title = 'Planning — AI risk and opportunity management', i1.article = 'Clause 6';
MERGE (i1)-[:PART_OF]->(iso)

MERGE (i2:StandardClause {id: 'ISO42001-8'})
  SET i2.standard_id = 'ISO-42001', i2.title = 'Operation — AI system development controls', i2.article = 'Clause 8';
MERGE (i2)-[:PART_OF]->(iso)

MERGE (i3:StandardClause {id: 'ISO42001-9'})
  SET i3.standard_id = 'ISO-42001', i3.title = 'Performance evaluation', i3.article = 'Clause 9';
MERGE (i3)-[:PART_OF]->(iso)

// NIST AIRF
MERGE (n1:StandardClause {id: 'NIST-GOVERN'})
  SET n1.standard_id = 'NIST-AIRF', n1.title = 'GOVERN — Policies, processes, accountability', n1.article = 'GOVERN';
MERGE (n1)-[:PART_OF]->(nist)

MERGE (n2:StandardClause {id: 'NIST-MAP'})
  SET n2.standard_id = 'NIST-AIRF', n2.title = 'MAP — Context and risk categorisation', n2.article = 'MAP';
MERGE (n2)-[:PART_OF]->(nist)

MERGE (n3:StandardClause {id: 'NIST-MEASURE'})
  SET n3.standard_id = 'NIST-AIRF', n3.title = 'MEASURE — Analysis and monitoring', n3.article = 'MEASURE';
MERGE (n3)-[:PART_OF]->(nist)

MERGE (n4:StandardClause {id: 'NIST-MANAGE'})
  SET n4.standard_id = 'NIST-AIRF', n4.title = 'MANAGE — Risk response and recovery', n4.article = 'MANAGE';
MERGE (n4)-[:PART_OF]->(nist)

// ── Map questions to standards (sample key mappings) ─────────────────────────
MATCH (q:AssessmentQuestion {id: 'PIA-11'}), (s:StandardClause {id: 'EU-AIA-ART14'}) MERGE (q)-[:MAPS_TO]->(s);
MATCH (q:AssessmentQuestion {id: 'ETH-03'}), (s:StandardClause {id: 'EU-AIA-ART13'}) MERGE (q)-[:MAPS_TO]->(s);
MATCH (q:AssessmentQuestion {id: 'MDL-03'}), (s:StandardClause {id: 'EU-AIA-ART15'}) MERGE (q)-[:MAPS_TO]->(s);
MATCH (q:AssessmentQuestion {id: 'DAT-02'}), (s:StandardClause {id: 'EU-AIA-ART10'}) MERGE (q)-[:MAPS_TO]->(s);
MATCH (q:AssessmentQuestion {id: 'REG-01'}), (s:StandardClause {id: 'EU-AIA-ART9'})  MERGE (q)-[:MAPS_TO]->(s);
MATCH (q:AssessmentQuestion {id: 'REG-02'}), (s:StandardClause {id: 'ISO42001-8'})   MERGE (q)-[:MAPS_TO]->(s);
MATCH (q:AssessmentQuestion {id: 'REG-03'}), (s:StandardClause {id: 'NIST-GOVERN'})  MERGE (q)-[:MAPS_TO]->(s);
MATCH (q:AssessmentQuestion {id: 'MDL-02'}), (s:StandardClause {id: 'NIST-MEASURE'}) MERGE (q)-[:MAPS_TO]->(s);
MATCH (q:AssessmentQuestion {id: 'AGT-03'}), (s:StandardClause {id: 'EU-AIA-ART14'}) MERGE (q)-[:MAPS_TO]->(s);
MATCH (q:AssessmentQuestion {id: 'ETH-01'}), (s:StandardClause {id: 'NIST-MAP'})     MERGE (q)-[:MAPS_TO]->(s);

// ── Control Recommendations ───────────────────────────────────────────────────
MERGE (cr1:ControlRecommendation {id: 'CR-PIA-DPIA'})
  SET cr1.description = 'Conduct a Data Protection / Privacy Impact Assessment using the approved PIA template',
      cr1.domain = 'Privacy & PIA', cr1.effort = 'medium';
MATCH (q:AssessmentQuestion {id: 'PIA-10'}), (cr:ControlRecommendation {id: 'CR-PIA-DPIA'}) MERGE (q)-[:HAS_CONTROL]->(cr);

MERGE (cr2:ControlRecommendation {id: 'CR-AGT-HITL'})
  SET cr2.description = 'Implement human-in-the-loop review gates for all high-risk agent decisions',
      cr2.domain = 'Agentic AI', cr2.effort = 'high';
MATCH (q:AssessmentQuestion {id: 'AGT-03'}), (cr:ControlRecommendation {id: 'CR-AGT-HITL'}) MERGE (q)-[:HAS_CONTROL]->(cr);

MERGE (cr3:ControlRecommendation {id: 'CR-CYB-MFA'})
  SET cr3.description = 'Enforce MFA on all accounts with access to AI infrastructure and model management',
      cr3.domain = 'Cyber Security', cr3.effort = 'low';
MATCH (q:AssessmentQuestion {id: 'CYB-03'}), (cr:ControlRecommendation {id: 'CR-CYB-MFA'}) MERGE (q)-[:HAS_CONTROL]->(cr);

MERGE (cr4:ControlRecommendation {id: 'CR-MDL-CARD'})
  SET cr4.description = 'Publish a model card for all AI models in the enterprise model registry',
      cr4.domain = 'Model Risk', cr4.effort = 'medium';
MATCH (q:AssessmentQuestion {id: 'MDL-01'}), (cr:ControlRecommendation {id: 'CR-MDL-CARD'}) MERGE (q)-[:HAS_CONTROL]->(cr);

MERGE (cr5:ControlRecommendation {id: 'CR-ETH-BIAS'})
  SET cr5.description = 'Run bias evaluation toolkit (e.g. IBM AI Fairness 360) on training data and model predictions',
      cr5.domain = 'Ethics & Fairness', cr5.effort = 'high';
MATCH (q:AssessmentQuestion {id: 'ETH-01'}), (cr:ControlRecommendation {id: 'CR-ETH-BIAS'}) MERGE (q)-[:HAS_CONTROL]->(cr);

MERGE (cr6:ControlRecommendation {id: 'CR-SUP-DPA'})
  SET cr6.description = 'Execute AI-specific data processing addendum with all LLM/AI suppliers before go-live',
      cr6.domain = 'Supplier & Third Party', cr6.effort = 'medium';
MATCH (q:AssessmentQuestion {id: 'SUP-02'}), (cr:ControlRecommendation {id: 'CR-SUP-DPA'}) MERGE (q)-[:HAS_CONTROL]->(cr);

// ── Governance Patterns ───────────────────────────────────────────────────────
MERGE (gp1:GovernancePattern {id: 'GP-REGISTER'})
  SET gp1.name = 'Register: Log AI system in AI Registry before development begins',
      gp1.phase = 'Register', gp1.order = 1;

MERGE (gp2:GovernancePattern {id: 'GP-ASSESS'})
  SET gp2.name = 'Assess: Complete PIA, RAI Scorecard, and Supplier Risk Assessment',
      gp2.phase = 'Assess', gp2.order = 2;

MERGE (gp3:GovernancePattern {id: 'GP-REVIEW'})
  SET gp3.name = 'Review: Submit to ARB / AI Council for design review at architecture gate',
      gp3.phase = 'Review', gp3.order = 3;

MERGE (gp4:GovernancePattern {id: 'GP-ALIGN'})
  SET gp4.name = 'Align: Ensure compliance with EU AI Act, ISO 42001, NIST AIRF, and APPs',
      gp4.phase = 'Align', gp4.order = 4;

MERGE (gp5:GovernancePattern {id: 'GP-OPERATE'})
  SET gp5.name = 'Operate: Monitor model drift, bias, and performance post-deployment',
      gp5.phase = 'Operate', gp5.order = 5;

// Map patterns to questions
MATCH (q:AssessmentQuestion {id: 'PIA-10'}), (gp:GovernancePattern {id: 'GP-ASSESS'}) MERGE (q)-[:FOLLOWS_PATTERN]->(gp);
MATCH (q:AssessmentQuestion {id: 'REG-01'}), (gp:GovernancePattern {id: 'GP-ALIGN'})  MERGE (q)-[:FOLLOWS_PATTERN]->(gp);
MATCH (q:AssessmentQuestion {id: 'ARB-01'}), (gp:GovernancePattern {id: 'GP-REVIEW'}) MERGE (q)-[:FOLLOWS_PATTERN]->(gp);
MATCH (q:AssessmentQuestion {id: 'MDL-03'}), (gp:GovernancePattern {id: 'GP-OPERATE'}) MERGE (q)-[:FOLLOWS_PATTERN]->(gp);
MATCH (q:AssessmentQuestion {id: 'ETH-04'}), (gp:GovernancePattern {id: 'GP-REGISTER'}) MERGE (q)-[:FOLLOWS_PATTERN]->(gp);
