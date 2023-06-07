import random
from fastapi import APIRouter, Response, status, Request, Body

# , , Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from models.employee import Employee
from typing import List

# from models import employee

router = APIRouter(prefix="/employee")


@router.get("/all")
def get_all_employees():
    employees = list(Employee.objects())
    print(f"{employees=}")
    return employees


@router.post("")
async def create_employee(request: Request):
    data = await request.json()
    employee = Employee(
        employee_id=data.get("id_employee"),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        role = [role for role in data.get("role")],
        department=[d for d in data.get("department")],
        email=data.get("email"),
        phone_number=data.get("phone_number"),
        start_date = data.get("start_date"),
        tags = [t for t in data.get("tags")],
        frontally = [f for f in data.get("frontally")],
        days_in_home=data.get("days_in_home"),
        schedule=[s for s in data.get("schedule")],
        user_name=data.get("user_name"),
        password=data.get("password")
    )
    employee.save()
    print(data)
    # employee = jsonable_encoder(employee)
    # new_employee = request.app.database["employees"].insert_one(employee)
    # created_employee = request.app.database["employees"].find_one(
    #     {"_id": new_employee.inserted_id}
    # )

    # return created_employee
    return "OK"

@router.get('/id_employee')
def get_employee_by_name(first_name: str):
    employee = Employee.find_one(first_name=first_name)
    if not employee:
        raise Exception("The employee isn't exist")
    return employee

@router.put('/id_employee')
async def update_employee_by_name(id_employee: str, employee: Employee):
    result = list(Employee.objects()).update_one({"id_employee": id_employee}, {"$set": employee.dict()}).save()
    
    if result.matched_count == 0:
        raise Exception("Employee not found")
    updated_employee = Employee.objects(id_employee=id_employee).first()
    updated_employee.save()  # Save the changes to the database
    return {"message": "Employee updated successfully"}

@router.delete('/<id_employee>')
async def delete_employee_by_id(id_employee: str):
    result = list(Employee.objects).find_one(id_employee==id_employee).delete_one({"id": id}).save()
    
    if result.deleted_count == 0:
        raise Exception("Employee not found")
    result.save()
    return {"message": "Employee deleted successfully"}
    

    



