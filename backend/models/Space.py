from mongoengine import connect, Document, StringField,  EnumField, DateTimeField, ListField, ListField,IntField
import datetime 
import random


class Space(Document):
    offices= ListField(StringField(max_length=50),required=True)
    location=StringField(required=True)
    floors=IntField(required=True)
    description=StringField()
