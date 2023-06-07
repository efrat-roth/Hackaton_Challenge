# credit: https://github.com/mongodb-developer/pymongo-fastapi-crud
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import dotenv_values
from routes import employeeRoutes as employeeRoutes
from routes import officeRoutes as officeRouter
from routes import spaceRoutes as spaceRouter
from routes import scheduleRoutes as scheduleRouter


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
    app.mongodb_client = MongoClient(
        os.getenv("MONGO_IP"),
        username=os.getenv("MONGO_USER"),
        password=os.getenv("MONGO_PASSWORD"),
    )
    app.database = app.mongodb_client["bootcamp"]


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(task_router, tags=["tasks"], prefix="/api/v1/tasks")
app.include_router(project_router, tags=["projects"], prefix="/api/v1/projects")