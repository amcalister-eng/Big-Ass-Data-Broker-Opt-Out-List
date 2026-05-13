import os
from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from app.services import graph_service_sqlite as gs, document_parser
from app.core.config import settings

router = APIRouter()


@router.post("")
async def create_project(
    name: str = Form(...),
    description: str = Form(...),
    team: str = Form(""),
    business_unit: str = Form(""),
    file: UploadFile = File(None),
):
    project = gs.create_project(name, description, team, business_unit)

    if file:
        file_path = await document_parser.save_upload(file, project["id"])
        text = document_parser.extract_text(file_path)
        gs.store_document_text(project["id"], text, file.filename)
        project["file_name"] = file.filename

    return project


@router.get("")
async def list_projects():
    return gs.list_projects()


@router.get("/{project_id}")
async def get_project(project_id: str):
    project = gs.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
