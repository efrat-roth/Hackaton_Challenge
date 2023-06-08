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
    disconnect()
    pass
    # app.mongodb_client.close()


app.include_router(employee.router)
app.include_router(floor.router)
app.include_router(floor.router)

