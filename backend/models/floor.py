from enum import Enum
import datetime
import uuid
from pydantic import BaseModel, Field


class Floor(Document):
  #id_floor= stringField(required=True)
  num_floor=intField(required=True,max_length=4)
   num_cube=intField(required=True)

floor = Floor(num_floor=range(1,5))
floor.save()
floor=Floor(num_cube=range(0,50))
floor.save()
print('start')
print('Done! ')




