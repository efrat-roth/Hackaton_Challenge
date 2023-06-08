from enum import Enum
import datetime
import uuid
from pydantic import BaseModel, Field


class floor(BaseModel):
    id_floor= string Field(default_factory=uuid.uuid4, alias="_id")
    num_floor : int=Field(...)
   num_cube:int=Field(...)
  list_cubes: ListField=Field(...)
    department: str=Field(...)
    email: str=Field(...)
    phone_number:str=Field(...)
    start_date:datetime=Field(...)
    tags:str=Field(...)
    frontally:tuple=Field(...)
    hasPreferences:bool=Field(...)
    tags = ListField(StringField(max_length=50))



class Role(Enum):
    "Manager", 
    "Employee",
    "TeamManager",
    "Receptionist",
    "SuperVisor",
    "Temporary"
List_names=["avishag","yael","shirel","tehila","rinat","avigailTen"]
