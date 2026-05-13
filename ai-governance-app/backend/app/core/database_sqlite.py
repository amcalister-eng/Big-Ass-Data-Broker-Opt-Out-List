"""
SQLite backend — drop-in replacement for Neo4j for local dev/demo.
Stores graph data in a local SQLite file.
"""
import sqlite3
import json
import os
from pathlib import Path

DB_PATH = os.environ.get("SQLITE_PATH", "/tmp/ai_governance.db")


def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.executescript("""
    CREATE TABLE IF NOT EXISTS risk_domains (
        id TEXT PRIMARY KEY, name TEXT, color TEXT, ord INTEGER
    );
    CREATE TABLE IF NOT EXISTS questions (
        id TEXT PRIMARY KEY, text TEXT, domain TEXT,
        risk_weight REAL, category TEXT, domain_id TEXT
    );
    CREATE TABLE IF NOT EXISTS standards (
        id TEXT PRIMARY KEY, name TEXT, version TEXT, jurisdiction TEXT
    );
    CREATE TABLE IF NOT EXISTS standard_clauses (
        id TEXT PRIMARY KEY, standard_id TEXT, title TEXT, article TEXT
    );
    CREATE TABLE IF NOT EXISTS question_standards (
        question_id TEXT, clause_id TEXT
    );
    CREATE TABLE IF NOT EXISTS control_recommendations (
        id TEXT PRIMARY KEY, description TEXT, domain TEXT, effort TEXT
    );
    CREATE TABLE IF NOT EXISTS question_controls (
        question_id TEXT, control_id TEXT
    );
    CREATE TABLE IF NOT EXISTS governance_patterns (
        id TEXT PRIMARY KEY, name TEXT, phase TEXT, ord INTEGER
    );
    CREATE TABLE IF NOT EXISTS question_patterns (
        question_id TEXT, pattern_id TEXT
    );
    CREATE TABLE IF NOT EXISTS projects (
        id TEXT PRIMARY KEY, name TEXT, description TEXT,
        team TEXT, business_unit TEXT, document_text TEXT,
        file_name TEXT, created_at TEXT
    );
    CREATE TABLE IF NOT EXISTS assessments (
        id TEXT PRIMARY KEY, project_id TEXT, status TEXT,
        rai_score REAL, risk_tier TEXT, overall_confidence REAL,
        requires_adrb INTEGER, requires_ai_council INTEGER,
        created_at TEXT, completed_at TEXT
    );
    CREATE TABLE IF NOT EXISTS coverage (
        assessment_id TEXT, question_id TEXT, confidence REAL,
        evidence TEXT, gap_summary TEXT, risk_rating TEXT,
        PRIMARY KEY (assessment_id, question_id)
    );
    """)
    conn.commit()
    conn.close()
