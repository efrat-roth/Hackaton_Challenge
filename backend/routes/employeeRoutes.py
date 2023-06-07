from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import employeeModel

employeeRoutes = APIRouter()
@employeeRoutes.post("", response_description="Create a new employee", status_code=status.HTTP_201_CREATED, response_model=employeeModel)
def create_employee(request: Request, employee: Employee = Body(...)):
    employee = jsonable_encoder(employee)
    new_employee = request.app.database["employees"].insert_one(employee)
    created_employee = request.app.database["employees"].find_one(
        {"_id": new_employee.inserted_id}
    )

    return created_employee


@employeeRoutes.get("", response_description="List all employees", response_model=List[employeeModel])
def list_employees(request: Request):
    employees = list(request.app.database["employees"].find(limit=100))
    return employees


@employeeRoutes.get("/{id}", response_description="Get a single employee by id", response_model=employeeModel)
def find_employee(id: str, request: Request):
    if (employee := request.app.database["employees"].find_one({"_id": id})) is not None:
        return employee

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Employee with ID {id} not found")


@employeeRoutes.put("/{id}", response_description="Update a Employee", response_model=employeeModel)
def update_employee(id: str, request: Request, employee: EmployeeUpdate = Body(...)):
    employee = {k: v for k, v in employee.dict().items() if v is not None}

    if len(employee) >= 1:
        update_result = request.app.database["employees"].update_one(
            {"_id": id}, {"$set": employee}
        )

        if update_result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with ID {id} not found")

    if (
        existing_employee := request.app.database["employee"].find_one({"_id": id})
    ) is not None:
        return existing_employee

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Employee with ID {id} not found")


@employeeRoutes.delete("/{id}", response_description="Delete a employee")
def delete_employee(id: str, request: Request, response: Response):
    delete_result = request.app.database["employees"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Employee with ID {id} not found")

