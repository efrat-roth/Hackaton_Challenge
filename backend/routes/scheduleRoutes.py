from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import scheduleModel

scheduleRouts = APIRouter()
@scheduleRouts.post("", response_description="Create a new schedule", status_code=status.HTTP_201_CREATED, response_model=employeeModel)
def create_schedule(request: Request, schedule: scheduleModel = Body(...)):
    schedule = jsonable_encoder(schedule)
    new_schedule = request.app.database["schedules"].insert_one(schedule)
    created_schedule = request.app.database["schedules"].find_one(
        {"_id": new_schedule.inserted_id}
    )

    return created_schedule


@scheduleRouts.get("", response_description="List all schedules", response_model=List[scheduleModel])
def list_employees(request: Request):
    offices = list(request.app.database["schedules"].find(limit=100))
    return offices


@scheduleRouts.get("/{id}", response_description="Get a single schedule by id", response_model=scheduleModel)
def find_schedule(id: str, request: Request):
    if (schedule := request.app.database["schedules"].find_one({"_id": id})) is not None:
        return schedule

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Schedule with ID {id} not found")


@scheduleRouts.put("/{id}", response_description="Update a Schedule", response_model=scheduleModel)
def update_schedule(id: str, request: Request, employee: scheduleUpdate = Body(...)):
    schedule = {k: v for k, v in schedule.dict().items() if v is not None}

    if len(schedule) >= 1:
        update_result = request.app.database["schedules"].update_one(
            {"_id": id}, {"$set": schedule}
        )

        if update_result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Schedule with ID {id} not found")

    if (
        existing_office := request.app.database["schedule"].find_one({"_id": id})
    ) is not None:
        return existing_schedule

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Schedule with ID {id} not found")


@scheduleRouts.delete("/{id}", response_description="Delete a schedule")
def delete_schedule(id: str, request: Request, response: Response):
    delete_result = request.app.database["schedules"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Schedule with ID {id} not found")

