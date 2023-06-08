from mongoengine import connect, Document, StringField,  EnumField, DateTimeField, ListField, ListField,IntField
from enum import Enum
import datetime 
import random


class Event(Document):   
    event_name=StringField(default="                                                        ")
    event_manage= DateTimeField(default=datetime.datetime.utcnow,required=True)
    startTime=DateTimeField(default=datetime.datetime.utcnow,required=True)
    endTime=DateTimeField(default=datetime.datetime.utcnow,required=True)



