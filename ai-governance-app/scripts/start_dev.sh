#!/usr/bin/env bash
# Start development environment
set -e

cd "$(dirname "$0")/.."

echo "==> Starting Neo4j..."
docker compose up -d neo4j

echo "==> Waiting for Neo4j to be healthy..."
until curl -s http://localhost:7474 > /dev/null; do sleep 2; done

echo "==> Seeding database..."
NEO4J_URI=bolt://localhost:7687 NEO4J_USER=neo4j NEO4J_PASSWORD=governance123 \
  python3 scripts/seed_db.py

echo "==> Starting backend..."
cd backend
pip install -r requirements.txt -q
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload &
BACKEND_PID=$!
cd ..

echo "==> Installing frontend dependencies..."
cd frontend
pnpm install
pnpm dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✓ Backend running at http://localhost:8000"
echo "✓ Frontend running at http://localhost:3000"
echo "✓ Neo4j browser at http://localhost:7474"
echo ""
echo "Press Ctrl+C to stop."
trap "kill $BACKEND_PID $FRONTEND_PID" EXIT
wait
