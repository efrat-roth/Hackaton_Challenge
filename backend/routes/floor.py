import random
from fastapi import APIRouter, Response, status, Request, Body

# , , Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from models.floor import Floor
from typing import List

router = APIRouter(prefix="/floor")


@router.get("/all")
def get_all_floors():
    floors = list(Floor.objects())
    print(f"{floors=}")
    return [ f.to_json() for f in floors]


@router.post("")
async def create_floor(request: Request):
    data = await request.json()
    floor = Floor(
        num_floor=data.get("num_floor"),
        num_cube=data.get("num_cube"),
    )
    floor.save()
    print(data)
    return "OK"

@router.get('/<num_floor>')
def get_office_by_name(num_floor: int):
    floor = Floor.find_one(num_floor==num_floor)
    if not floor:
        raise Exception("The floor isn't exist")
    return "OK"

@router.put('/<num_floor>')
def update_floor_by_num(num_floor: int):
    result = list(Floor.objects()).update_one({"num_floor": num_floor}, {"$set": floor.dict()})
    
    if result.matched_count == 0:
        raise Exception("floor not found")
    updated_floor = Floor.objects(num_floor=num_floor).first()
    updated_floor.save()  # Save the changes to the database
    return {"message": "Floor updated successfully"}

@router.delete('/<num_floor>')
def delete_office_by_name(num_floor: int):
    result = list(Floor.objects()).find_one(num_floor==num_floor).delete_one({"num_floor": num_floor}).save()
    
    if result.deleted_count == 0:
        raise Exception("Floor not found")
    result.save()
    return {"message": "Floor deleted successfully"}
    

    



