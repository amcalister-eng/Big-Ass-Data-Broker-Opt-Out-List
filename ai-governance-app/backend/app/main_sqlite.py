from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database_sqlite import init_db
from app.services.seed_sqlite import seed
from app.api import projects_sqlite, assessments_sqlite, chat_sqlite, reports_sqlite

app = FastAPI(title="AI Governance Mapping API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects_sqlite.router, prefix="/api/projects", tags=["projects"])
app.include_router(assessments_sqlite.router, prefix="/api/assessments", tags=["assessments"])
app.include_router(chat_sqlite.router, prefix="/api/chat", tags=["chat"])
app.include_router(reports_sqlite.router, prefix="/api/reports", tags=["reports"])


@app.on_event("startup")
def startup():
    init_db()
    seed()


@app.get("/health")
async def health():
    return {"status": "ok"}
