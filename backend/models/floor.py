from mongoengine import connect, Document, StringField,  EnumField, DateTimeField, ListField, ListField,IntField,BooleanField
from enum import Enum
import datetime 
import random


username = "manager"
password = "qwertyuiop"
hostname = "projectdatabase.gekhcz5.mongodb.net"
dbname = "floors"
# connect(dbname, username=username, password=password,
#              host = f"mongodb+srv://{hostname}"
#  )

class Floor(Document):
  num_floor=IntField(required=True,max_length=4)
  num_cube=IntField(required=True)

# for i in range(0,5):
#   floor = Floor(num_floor=i,num_cube=100)
#   floor.save()
def to_json(self):
    return{
        "num_floor": self.num_floor,
        "num_cube": self.num_cube;
    }


print('start1')
print('Done! ')




