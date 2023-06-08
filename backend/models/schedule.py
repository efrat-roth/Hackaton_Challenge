from mongoengine import connect, Document, StringField,  EnumField, DateTimeField, ListField, ListField,IntField
from enum import Enum
import datetime 
import random


class Schedule(Document):
    
    office_name=IntField(required=True)
    date= DateTimeField(default=datetime.datetime.utcnow,required=True)
    startTime=DateTimeField(default=datetime.datetime.utcnow,required=True)
    endTime=DateTimeField(default=datetime.datetime.utcnow,required=True)



