import random
from fastapi import APIRouter, Response, status, Request, Body

# , , Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from models.office import Office
from typing import List

router = APIRouter(prefix="/office")


@router.get("/all")
def get_all_offices():
    office = list(Office.objects())
    print(f"{offices=}")
    return offices


@router.post("")
async def create_office(request: Request):
    data = await request.json()
    office = Office(
        office_name=data.get("office_name"),
        location=data.get("location"),
        floor=data.get("floor"),
        capacity=data.get("capacity"),
    )
    office.save()
    print(data)
    return "OK"

@router.get('/office_name')
def get_office_by_name(office_name: str):
    office = Office.find_one(office_name=office_name)
    if not office:
        raise Exception("The office isn't exist")
    return office

@router.put('/office_name')
async def update_office_by_name(office_name: str, office: Office):
    result = list(Office.objects()).update_one({"office_name": office_name}, {"$set": office.dict()})
    
    if result.matched_count == 0:
        raise Exception("office not found")
    updated_office = Office.objects(office_name=office_name).first()
    updated_office.save()  # Save the changes to the database
    return {"message": "Office updated successfully"}

@router.delete('/<office_name>')
async def delete_office_by_name(office_name: str):
    result = list(Office.objects).find_one(office_name==office_name).delete_one({"office_name": office_name}).save()
    
    if result.deleted_count == 0:
        raise Exception("Office not found")
    result.save()
    return {"message": "Office deleted successfully"}
    

    



