import random
import requests
from fastapi import APIRouter, Response, status, Request, Body
from fastapi.encoders import jsonable_encoder
from models.employee import Employee
from typing import List
from models.sced_arr import ScedArr

router = APIRouter(prefix="/sced_arr")


@router.get("/all")
def get_all_sced():
    sced_arr = list(ScedArr.objects())
    print(f"{sced_arr=}")
    return [s.to_json() for s in sced_arr]


@router.post("")
async def create_employee(request: Request):
    data = await request.json()
    sced_arr = ScedArr(
        id_sced=data.get("id_sced"),
        employee_list=data.get("employee_list"),
    )
    sced_arr.save()
    print(data)
    return "OK"


@router.get("/<{id_sced}>")
def get_sced_by_id(id_sced: int):
    sced_arr = ScedArr.objects(id_sced=id_sced).first()
    if not sced_arr:
        raise Exception("The schedule isn't exist")
    return sced_arr.to_json()


@router.put("/id_sced")
def update_sced_by_id(id_sced: int):
    result = (
        list(ScedArr.objects())
        .update_one({"id_sced": id_sced}, {"$set": ScedArr.dict()})
        .save()
    )

    if result.matched_count == 0:
        raise Exception("id not found")
    updated_sced = ScedArr.objects(id_sced=id_sced).first()
    updated_sced.save()  # Save the changes to the database
    return {"message": "sced updated successfully"}


@router.delete("/< id_sced>")
def delete_employee_by_id(id_sced: int):
    result = list(Employee.objects).find_one(id_sced == id_sced).delete_one({"id": id})

    if result.deleted_count == 0:
        raise Exception("sced not found")
    result.save()
    return {"message": "sced deleted successfully"}


@router.put("/update_marks")
def update_marks(id_sced: int):
    result = (
        list(ScedArr.objects())
        .update_one({"id_sced": id_sced}, {"$set": ScedArr.dict()})
        .save()
        )

    if result.matched_count == 0:
        raise Exception("id not found")
    updated_sced = ScedArr.objects(id_sced=id_sced).first()
    updated_sced.save()  # Save the changes to the database
    return {"message": "sced updated successfully"}


@router.put("/employee/{employee_id}")
async def add_employee_to_list(request: Request, employee_id: str):
    print(f"{dir(request) = }")
    data = await request.json()
    print(f"{data=}")

    employee = Employee.objects(employee_id=int(employee_id)).first()
    if not employee:
        return "no employee has found"
    for attr, value in employee.to_json().items():
        # print(f"{attr}") 
        if attr in data:
            print(f"updating {attr} with {data.get(attr)}")
            setattr(employee, attr ,data.get(attr))
            # employee.update(attr=data.get(attr))
            # employee.first_name = data.get("first_name")
    
    print(f"{employee.to_json()}")
    employee.save()
    # employee.role = 
    
    # Employee.objects(employee_id=int(employee_id)).first()

    # if not employee:
    #     print("No one have found")
    # else:
    #     print(f"found: {employee=}")
    # if data.day_of_week < 0 or data.day_of_week > 4:
    #     raise ValueError("Invalid day of the week. Expected a number from 0 to 4.")

    # # Access the array in the data layer and add the employee to the corresponding list

    # requests.get("http://localhost:8000/sced_arr/1").json().employee_list[
    #     day_of_week
    # ].append(employee)
    return "OK"
