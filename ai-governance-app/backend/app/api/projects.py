import os
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from neo4j import AsyncSession
from app.core.database import get_session
from app.models.schemas import ProjectCreate, ProjectOut
from app.services import graph_service, document_parser
from app.core.config import settings

router = APIRouter()


@router.post("", response_model=ProjectOut)
async def create_project(
    name: str = Form(...),
    description: str = Form(...),
    team: str = Form(""),
    business_unit: str = Form(""),
    file: UploadFile = File(None),
    session: AsyncSession = Depends(get_session),
):
    project = await graph_service.create_project(session, name, description, team, business_unit)

    if file:
        file_path = await document_parser.save_upload(file, project["id"])
        text = document_parser.extract_text(file_path)
        # Store extracted text on project node
        await session.run(
            "MATCH (p:Project {id: $id}) SET p.document_text = $text, p.file_name = $fname",
            id=project["id"], text=text[:50000], fname=file.filename,
        )
        project["file_name"] = file.filename

    return project


@router.get("")
async def list_projects(session: AsyncSession = Depends(get_session)):
    return await graph_service.list_projects(session)


@router.get("/{project_id}")
async def get_project(project_id: str, session: AsyncSession = Depends(get_session)):
    project = await graph_service.get_project(session, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
