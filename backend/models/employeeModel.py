from enum import Enum
import datetime
import uuid
from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    first_name : str=Field(...)
    last_name:str=Field(...)
    role: Role=Field(...)
    department: str=Field(...)
    email: str=Field(...)
    phone_number:str=Field(...)
    start_date:datetime=Field(...)
    tags:str=Field(...)
    frontally:tuple=Field(...)
    hasPreferences:bool=Field(...)



class Role(Enum):
    "Manager", 
    "Employee",
    "TeamManager",
    "Receptionist",
    "SuperVisor",
    "Temporary"
