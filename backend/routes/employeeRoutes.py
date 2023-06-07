from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import employeeModel

routerP = APIRouter()
@routerP.post("", response_description="Create a new employee", status_code=status.HTTP_201_CREATED, response_model=Project)
def create_employee(request: Request, employee: Employee = Body(...)):
    employee = jsonable_encoder(employee)
    new_employee = request.app.database["employees"].insert_one(employee)
    created_employee = request.app.database["employees"].find_one(
        {"_id": new_employee.inserted_id}
    )

    return created_employee


@routerP.get("", response_description="List all projects", response_model=List[Project])
def list_projects(request: Request):
    projects = list(request.app.database["projects"].find(limit=100))
    return projects


@routerP.get("/{id}", response_description="Get a single project by id", response_model=Project)
def find_project(id: str, request: Request):
    if (Project := request.app.database["projects"].find_one({"_id": id})) is not None:
        return Project

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Project with ID {id} not found")


@routerP.put("/{id}", response_description="Update a Project", response_model=Project)
def update_task(id: str, request: Request, project: ProjectUpdate = Body(...)):
    project = {k: v for k, v in project.dict().items() if v is not None}

    if len(project) >= 1:
        update_result = request.app.database["projects"].update_one(
            {"_id": id}, {"$set": project}
        )

        if update_result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Project with ID {id} not found")

    if (
        existing_project := request.app.database["projects"].find_one({"_id": id})
    ) is not None:
        return existing_project

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Project with ID {id} not found")


@routerP.delete("/{id}", response_description="Delete a project")
def delete_task(id: str, request: Request, response: Response):
    delete_result = request.app.database["projects"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Project with ID {id} not found")

