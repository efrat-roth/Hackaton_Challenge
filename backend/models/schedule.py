from mongoengine import connect, Document, StringField,  EnumField, DateTimeField, ListField, ListField,IntField,BooleanField
from enum import Enum
import datetime 
import random




class Schedule(Document):
    Schedule_id=StringField(required=True)
    home=BooleanField()
    office=BooleanField()
    num_floor=IntField()
