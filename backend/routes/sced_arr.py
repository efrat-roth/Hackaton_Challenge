import random
from fastapi import APIRouter, Response, status, Request, Body
from fastapi.encoders import jsonable_encoder
from models.employee import Employee
from typing import List
from models.scedArr import ScedArr

router = APIRouter(prefix="/Sced_arr")


@router.get("/all")
def get_all_sced():
    sced_arrr = list(ScedArr.objects())
    print(f"{sced_arrr=}")
    return sced_arrr


@router.post("")
async def create_employee(request: Request):
    data = await request.json()
    sced_arrr = Sced_arr(
        employee_list=data.get("id_sced"),
    )
    sced_arrr.save()
    print(data)
    return "OK"


@router.put("/ id_sced")
def update_employee_by_id(id_sced: int, sced_arr: ScedArr):
    result = (
        list(scedArr.objects())
        .update_one({"id_sced": id_sced}, {"$set": scedArr.dict()})
        .save()
    )

    if result.matched_count == 0:
        raise Exception("id not found")
    updated_sced = ScedArr.objects(id_employee=id_employee).first()
    updated_sced.save()  # Save the changes to the database
    return {"message": "sced updated successfully"}


@router.delete("/< id_sced>")
def delete_employee_by_id(id_sced: int):
    result = (
        list(Employee.objects)
        .find_one(id_employee == id_employee)
        .delete_one({"id": id})
    )

    if result.deleted_count == 0:
        raise Exception("sced not found")
    result.save()
    return {"message": "sced deleted successfully"}
