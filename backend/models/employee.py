from mongoengine import (
    connect,
    Document,
    StringField,
    EnumField,
    DateTimeField,
    ListField,
    ListField,
    IntField,
    BooleanField,
)
from enum import Enum
from pydantic import BaseModel, Field
import datetime
import random


class Role(Enum):
    Manager = 1
    Employee = 2
    TeamManager = 3
    Receptionist = 4
    SuperVisor = 5
    Temporary = 6


class HiTechClass(Enum):
    SOFTWARE_ENGINEER = 1
    DATA_SCIENTIST = 2
    PRODUCT_MANAGER = 3
    UX_DESIGNER = 4
    NETWORK_ENGINEER = 5


class Employee(Document):
    employee_id = IntField(required=True)
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=False)
    # role = EnumField(Role, required=True)
    # department = EnumField(HiTechClass, required=True)
    email = StringField(max_length=50)
    phone_number = StringField(max_length=50)
    start_date = DateTimeField(default=datetime.datetime.utcnow)
    tags = ListField(StringField(max_length=50))
    days_in_home = IntField(required=True)
    meet = BooleanField(required=True)
    grade = IntField(required=True, default=0)
    floors = ListField(max_length=5)
    space = ListField(max_length=5)
    user_name = StringField(required=True)
    password = StringField(require=True)

    def __str__(self):
        return f"<{self.first_name} - {self.last_name} ({self.employee_id})>"
    

    def to_json(self):
        return {
            "employee_id": self.employee_id,
            "first_name":self.first_name,
            "last_name": self.last_name,
            # "role": self.role,
            # "department" :self.department,
            "email" : self.email,
            "phone_number": self.phone_number,
            "start_date": self.start_date,
            "tags" : self.tags,
            "days_in_home":self.days_in_home,
            "meet":self.meet,
            "grade" : self.grade,
            "floors": self.floors,
            "space":self.space,
            "user_name": self.user_name,
            "password": self.password
}



#connect(dbname, username=username, password=password, host=f"mongodb+srv://{hostname}")








#employee = Employee(employee_id="325528388", first_name="Avigail", last_name="Cohen",role=Role.Receptionist,department=HiTechClass(3),
#email="avigailcohen17@gmail.com",phone_number="0545476488",start_date=datetime.datetime.now(),tags=["python", "react", "css"],frontally=[False,19],days_in_home=6,meet=False,grade=2,user_name="Avigail",password="325528388")
#employee.save()

