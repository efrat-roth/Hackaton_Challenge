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
    Manager = (1,)
    Employee = (2,)
    TeamManager = (3,)
    Receptionist = (4,)
    SuperVisor = (5,)
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
    role = EnumField(Role, required=True)
    department = EnumField(HiTechClass, required=True)
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

    def to_json(self):
        return {
            "employee_id": self.employee_id,
            "first_name":self.first_name,
    "last_name": self.last_name,
    "role": self.role,
    "department" :self.department,
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


def generate_random_date():
    start_date = datetime.date(2017, 1, 1)  # Define your desired start date
    end_date = datetime.date(2022, 12, 31)  # Define your desired end date
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)
    random_date = start_date + datetime.timedelta(days=random_days)
    return random_date


username = "manager"
password = "qwertyuiop"
hostname = "projectdatabase.gekhcz5.mongodb.net"
dbname = "employees"
#connect(dbname, username=username, password=password, host=f"mongodb+srv://{hostname}")


# List_names=["avishag","yael","shirel","tehila","rinat","avigailTen"]

List_tagsBac = ["Python", "Java", "Databases", "API Design", "Microservices", "Testing"]

List_tagFro = [
    "HTML/CSS",
    "JavaScript",
    "UI/UX Design",
    "Frontend Frameworks",
    "Responsive Design",
    "Testing & Debugging",
]
List_lists = [List_tagsBac, List_tagFro]
departments = list(HiTechClass)


employee = Employee(employee_id="214430035", first_name="Efrat", last_name="Roth",role=Role.Manager,department=HiTechClass(1),
email="efratroth15@gmail.com", phone_number="0583280266",start_date=datetime.datetime.now(),tags=["c#", "visual"],days_in_home=5, meet=True,grade=23,user_name="Efrat",password="214430035")
employee.save()

#employee = Employee(employee_id="325528388", first_name="Avigail", last_name="Cohen",role=Role.Receptionist,department=HiTechClass(3),
#email="avigailcohen17@gmail.com",phone_number="0545476488",start_date=datetime.datetime.now(),tags=["python", "react", "css"],frontally=[False,19],days_in_home=6,meet=False,grade=2,user_name="Avigail",password="325528388")
#employee.save()
#for i in range(7):
# tags = list(List_lists[i % 2])
#random.shuffle(tags)
#employee = Employee(employee_id=str(i), first_name=List_names[i%6], last_name="test",
 #                 role=random.choice(list(Role)),department=(departments[i%5]),
  #               email=List_names[i%6] +str(i)+ "@gmail.com",
   #             phone_number="0583280"+str(i/100)+str(i%10/10)+str(i%100),start_date=generate_random_date(),
    #           tags=tags,days_in_home=i%5,meet=i%9==0,grade=i%25,schedule=[],user_name=List_names[i%6], password=str(i))
#employee.save()
print("start")
print("Done! ")
