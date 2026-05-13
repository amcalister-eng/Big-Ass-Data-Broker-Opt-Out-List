from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import close_driver
from app.api import projects, assessments, chat, reports


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await close_driver()


app = FastAPI(
    title="AI Governance Mapping API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects.router, prefix="/api/projects", tags=["projects"])
app.include_router(assessments.router, prefix="/api/assessments", tags=["assessments"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])


@app.get("/health")
async def health():
    return {"status": "ok"}
