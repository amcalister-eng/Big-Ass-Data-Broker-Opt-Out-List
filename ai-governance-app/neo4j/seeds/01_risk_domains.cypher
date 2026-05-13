// ── Risk Domains ──────────────────────────────────────────────────────────────
MERGE (d1:RiskDomain {id: 'RD-PIA'})
  SET d1.name = 'Privacy & PIA', d1.color = '#8b5cf6', d1.order = 1;

MERGE (d2:RiskDomain {id: 'RD-SUP'})
  SET d2.name = 'Supplier & Third Party', d2.color = '#06b6d4', d2.order = 2;

MERGE (d3:RiskDomain {id: 'RD-AGT'})
  SET d3.name = 'Agentic AI', d3.color = '#f59e0b', d3.order = 3;

MERGE (d4:RiskDomain {id: 'RD-CYB'})
  SET d4.name = 'Cyber Security', d4.color = '#ef4444', d4.order = 4;

MERGE (d5:RiskDomain {id: 'RD-ETH'})
  SET d5.name = 'Ethics & Fairness', d5.color = '#ec4899', d5.order = 5;

MERGE (d6:RiskDomain {id: 'RD-DAT'})
  SET d6.name = 'Data Governance', d6.color = '#10b981', d6.order = 6;

MERGE (d7:RiskDomain {id: 'RD-MDL'})
  SET d7.name = 'Model Risk', d7.color = '#6366f1', d7.order = 7;

MERGE (d8:RiskDomain {id: 'RD-OPS'})
  SET d8.name = 'Operational Risk', d8.color = '#84cc16', d8.order = 8;

MERGE (d9:RiskDomain {id: 'RD-REG'})
  SET d9.name = 'Regulatory & Legal', d9.color = '#f97316', d9.order = 9;

MERGE (d10:RiskDomain {id: 'RD-ARB'})
  SET d10.name = 'ARB / Agentic Review', d10.color = '#14b8a6', d10.order = 10;
