import uuid
from pydantic import BaseModel, Field


class Office(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str= Field(...)
    location: str=Field(...)
    floor:int= Field(...)
    capacity:int= Field(...)



