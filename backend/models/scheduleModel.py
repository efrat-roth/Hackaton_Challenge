
import datetime
import uuid
from pydantic import BaseModel, Field


class Schedule(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    officeId: int= Field(...)
    date: datetime=Field(...)
    startTime:datetime= Field(...)
    endTime:datetime= Field(...)



