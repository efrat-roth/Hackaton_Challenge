from mongoengine import connect, Document, StringField,  EnumField, DateTimeField, ListField, ListField,IntField,ReferenceField
from enum import Enum
import datetime 
import random
from models.employee import Employee

class ScedArr(Document):
    id_sced=IntField(required=True,default=1)
    employee_list = ListField(ListField(ReferenceField(Employee)),required=True)

def to_json(self):
    return{
        "id_sced":self.id_sced,
        "employee_list":self.employee_list
    }