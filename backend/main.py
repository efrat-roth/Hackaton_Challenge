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
    connect(
        dbname, username=username, password=password, host=f"mongodb+srv://{hostname}"
    )


@app.on_event("shutdown")
def shutdown_db_client():
    disconnect()
    pass
    app.mongodb_client.close()
# def generate_random_date():
#     start_date = datetime.date(2017, 1, 1)  # Define your desired start date
#     end_date = datetime.date(2022, 12, 31)  # Define your desired end date
#     days_between = (end_date - start_date).days
#     random_days = random.randint(0, days_between)
#     random_date = start_date + datetime.timedelta(days=random_days)
#     return random_date
# departments = list(HiTechClass)

# username = "manager"
# password = "qwertyuiop"
# hostname = "projectdatabase.gekhcz5.mongodb.net"
# dbname = "employees"
# List_names=["avishag","yael","shirel","tehila","rinat","avigailTen"]

# List_tagsBac = ["Python", "Java", "Databases", "API Design", "Microservices", "Testing"]

# List_tagFro = [
#     "HTML/CSS",
#     "JavaScript",
#     "UI/UX Design",
#     "Frontend Frameworks",
#     "Responsive Design",
#     "Testing & Debugging",
# ]
# List_lists = [List_tagsBac, List_tagFro]
# for i in range(7):
        
#     tags = list(List_lists[i % 2])
#     random.shuffle(tags)
#     employee = Employee(employee_id=str(i), first_name=List_names[i%6], last_name=List_names[i%5+1],
#                 email=List_names[i%6] +str(i)+ "@gmail.com",
#                phone_number="0583280"+str(i/100)+str(i%10/10)+str(i%100),start_date=generate_random_date(),
#               tags=tags,days_in_home=i%5,meet=i%9==0,grade=i%25,floors=[i%2,0,i%2,1,i%2],space=[i,i+1,i+2,i+3],user_name=List_names[i%6], password=str(i))
# employee.save()
# print("start")
# print("Done! ")


app.include_router(employee.router)
app.include_router(floor.router)
app.include_router(sced_arr.router)
