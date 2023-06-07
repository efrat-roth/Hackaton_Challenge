# credit: https://github.com/mongodb-developer/pymongo-fastapi-crud
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import dotenv_values
from mongoengine import connect
from routes import employee
# from routes import employeeRoutes as employeeRoutes
# from routes import officeRoutes as officeRouter
# from routes import spaceRoutes as spaceRouter
# from routes import scheduleRoutes as scheduleRouter


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
    dbname = "lol"
    connect(dbname, username=username, password=password,
        host = f"mongodb+srv://{hostname}"
    )

@app.on_event("shutdown")
def shutdown_db_client():
    pass
    # app.mongodb_client.close()


app.include_router(employee.router)
# app.include_router(task_router, tags=["tasks"], prefix="/api/v1/tasks")
# app.include_router(project_router, tags=["projects"], prefix="/api/v1/projects")
