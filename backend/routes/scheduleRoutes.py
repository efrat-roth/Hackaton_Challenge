from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import scheduleModel

routerP = APIRouter()
@routerP.post("", response_description="Create a new office", status_code=status.HTTP_201_CREATED, response_model=employeeModel)
def create_schedule(request: Request, schedule: Schedule = Body(...)):
    schedule = jsonable_encoder(schedule)
    new_schedule = request.app.database["schedules"].insert_one(schedule)
    created_office = request.app.database["schedules"].find_one(
        {"_id": new_schedule.inserted_id}
    )

    return created_office


@routerP.get("", response_description="List all schedules", response_model=List[scheduleModel])
def list_employees(request: Request):
    offices = list(request.app.database["schedules"].find(limit=100))
    return offices


@routerP.get("/{id}", response_description="Get a single office by id", response_model=officeModel)
def find_employee(id: str, request: Request):
    if (office := request.app.database["offices"].find_one({"_id": id})) is not None:
        return office

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Office with ID {id} not found")


@routerP.put("/{id}", response_description="Update a Office", response_model=officeModel)
def update_office(id: str, request: Request, employee: officeUpdate = Body(...)):
    office = {k: v for k, v in office.dict().items() if v is not None}

    if len(office) >= 1:
        update_result = request.app.database["offices"].update_one(
            {"_id": id}, {"$set": office}
        )

        if update_result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Office with ID {id} not found")

    if (
        existing_office := request.app.database["office"].find_one({"_id": id})
    ) is not None:
        return existing_office

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Office with ID {id} not found")


@routerP.delete("/{id}", response_description="Delete a office")
def delete_office(id: str, request: Request, response: Response):
    delete_result = request.app.database["offices"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Office with ID {id} not found")

