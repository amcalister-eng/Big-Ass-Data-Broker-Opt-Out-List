// ── Unique constraints ────────────────────────────────────────────────────────
CREATE CONSTRAINT project_id_unique IF NOT EXISTS
  FOR (p:Project) REQUIRE p.id IS UNIQUE;

CREATE CONSTRAINT assessment_id_unique IF NOT EXISTS
  FOR (a:ProjectAssessment) REQUIRE a.id IS UNIQUE;

CREATE CONSTRAINT risk_domain_id_unique IF NOT EXISTS
  FOR (d:RiskDomain) REQUIRE d.id IS UNIQUE;

CREATE CONSTRAINT question_id_unique IF NOT EXISTS
  FOR (q:AssessmentQuestion) REQUIRE q.id IS UNIQUE;

CREATE CONSTRAINT standard_id_unique IF NOT EXISTS
  FOR (s:GovernanceStandard) REQUIRE s.id IS UNIQUE;

CREATE CONSTRAINT clause_id_unique IF NOT EXISTS
  FOR (c:StandardClause) REQUIRE c.id IS UNIQUE;

CREATE CONSTRAINT trigger_id_unique IF NOT EXISTS
  FOR (t:Trigger) REQUIRE t.id IS UNIQUE;

CREATE CONSTRAINT control_id_unique IF NOT EXISTS
  FOR (c:ControlRecommendation) REQUIRE c.id IS UNIQUE;

CREATE CONSTRAINT pattern_id_unique IF NOT EXISTS
  FOR (gp:GovernancePattern) REQUIRE gp.id IS UNIQUE;

CREATE CONSTRAINT privacy_risk_id_unique IF NOT EXISTS
  FOR (pr:PrivacyRisk) REQUIRE pr.id IS UNIQUE;

CREATE CONSTRAINT engineering_item_id_unique IF NOT EXISTS
  FOR (e:EngineeringChecklistItem) REQUIRE e.id IS UNIQUE;

CREATE CONSTRAINT cyber_control_id_unique IF NOT EXISTS
  FOR (cc:CyberControl) REQUIRE cc.id IS UNIQUE;

// ── Indexes ───────────────────────────────────────────────────────────────────
CREATE INDEX question_domain_idx IF NOT EXISTS
  FOR (q:AssessmentQuestion) ON (q.domain);

CREATE INDEX project_name_idx IF NOT EXISTS
  FOR (p:Project) ON (p.name);
