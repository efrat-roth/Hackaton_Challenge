from mongoengine import connect, Document, StringField,  EnumField, DateTimeField, ListField, ListField,IntField
from enum import Enum
import datetime 
import random


class Office(Document):
    office_name= StringField(required=True)
    location=StringField(required=True)
    floor=IntField(required=True)
    capacity=IntField(required=True)



