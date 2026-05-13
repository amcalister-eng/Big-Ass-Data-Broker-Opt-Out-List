#!/usr/bin/env python3
"""
Seed the Neo4j graph database with governance schema and all question data.
Run after Neo4j is up: python scripts/seed_db.py
"""
import os
import sys
from pathlib import Path
from neo4j import GraphDatabase

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "governance123")

SEED_DIR = Path(__file__).parent.parent / "neo4j"
SCHEMA_DIR = SEED_DIR / "schema"
SEEDS_DIR = SEED_DIR / "seeds"


def run_cypher_file(session, path: Path):
    text = path.read_text()
    # Split on semicolon, run each statement
    statements = [s.strip() for s in text.split(";") if s.strip() and not s.strip().startswith("//")]
    for stmt in statements:
        if stmt:
            try:
                session.run(stmt)
            except Exception as e:
                print(f"  WARN: {e} in {path.name}")


def main():
    print(f"Connecting to Neo4j at {NEO4J_URI}...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    with driver.session() as session:
        # Schema / constraints first
        for f in sorted(SCHEMA_DIR.glob("*.cypher")):
            print(f"  Schema: {f.name}")
            run_cypher_file(session, f)

        # Seed data in order
        for f in sorted(SEEDS_DIR.glob("*.cypher")):
            print(f"  Seed: {f.name}")
            run_cypher_file(session, f)

    driver.close()
    print("Done. Graph database seeded successfully.")


if __name__ == "__main__":
    main()
