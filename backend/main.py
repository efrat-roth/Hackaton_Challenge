# credit: https://github.com/mongodb-developer/pymongo-fastapi-crud
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import dotenv_values
from mongoengine import connect, disconnect
from routes import employee
from routes import floor as floor
from routes import sced_arr
from models.employee import Employee
from models.employee import Role
from models.employee import HiTechClass
from enum import Enum
from pydantic import BaseModel, Field
import datetime
import random



dotenv_values(".env")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_db_client():
    username = "manager"
    password = "qwertyuiop"
    hostname = "projectdatabase.gekhcz5.mongodb.net"
    dbname = "employee"
    print("Connecting to DB")
    connect(dbname, username=username, password=password,
        host = f"mongodb+srv://{hostname}"
    )
    employee = Employee(employee_id="214430035", first_name="Efrat", last_name="Roth",role=Role.Manager,department=HiTechClass(1),
    email="efratroth15@gmail.com", phone_number="0583280266",start_date=datetime.datetime.now(),tags=["c#", "visual"],days_in_home=5, meet=True,grade=23,user_name="Efrat",password="214430035")
    employee.save()

@app.on_event("shutdown")
def shutdown_db_client():
    disconnect()
    pass
    # app.mongodb_client.close()

app.include_router(employee.router)
app.include_router(floor.router)
app.include_router(sced_arr.router)
