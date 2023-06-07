from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import spacedModel

spaceRouts = APIRouter()
@spaceRouts.post("", response_description="Create a new space", status_code=status.HTTP_201_CREATED, response_model=spacedModel)
def create_space(request: Request, schedule: spaceModel = Body(...)):
    schedule = jsonable_encoder(schedule)
    new_space = request.app.database["spaces"].insert_one(schedule)
    created_schedule = request.app.database["spaces"].find_one(
        {"_id": new_space.inserted_id}
    )

    return created_schedule


@spaceRouts.get("", response_description="List all spaces", response_model=List[spacedModel])
def list_spaces(request: Request):
    spaces = list(request.app.database["spaces"].find(limit=100))
    return spaces


@spaceRouts.get("/{id}", response_description="Get a single spaces by id", response_model=spacedModel)
def find_schedule(id: str, request: Request):
    if (space := request.app.database["spaces"].find_one({"_id": id})) is not None:
        return space

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"space with ID {id} not found")


@spaceRouts.put("/{id}", response_description="Update a Space", response_model=spacedModel)
def update_space(id: str, request: Request, employee: spaceUpdate = Body(...)):
    space = {k: v for k, v in space.dict().items() if v is not None}

    if len(space) >= 1:
        update_result = request.app.database["spaces"].update_one(
            {"_id": id}, {"$set": space}
        )

        if update_result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Space with ID {id} not found")

    if (
        existing_space := request.app.database["space"].find_one({"_id": id})
    ) is not None:
        return existing_space

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Space with ID {id} not found")


@spaceRouts.delete("/{id}", response_description="Delete a space")
def delete_space(id: str, request: Request, response: Response):
    delete_result = request.app.database["spaces"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Space with ID {id} not found")

