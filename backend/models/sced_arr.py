from mongoengine import connect, Document, StringField,  EnumField, DateTimeField, ListField, ListField,IntField,BooleanField
from enum import Enum
import datetime 
import random
from models import employee

class ScedArr(Document):
    id_sced=IntField(required=True)
    employee_list = ListField(ListField(ReferenceField(employee)),required=True)