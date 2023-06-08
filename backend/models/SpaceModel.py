
import uuid
from pydantic import BaseModel, Field


class Space(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    offices: list= Field(...)
    location:str = Field(...)
    floors:int= Field(...)
    description:str= Field(...)


