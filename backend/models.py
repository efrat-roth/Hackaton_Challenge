class Employee:
    def __init__(self, first_name, last_name, role, department, email, phone_number, start_date, tags, status, preferences):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.department = department
        self.email = email
        self.phone_number = phone_number
        self.start_date = start_date
        self.tags = tags
        self.status = status
        self.preferences = preferences

class Office:
    def __init__(self, office_name, location, capacity, facilities):
        self.office_name = office_name
        self.location = location
        self.capacity = capacity
        self.facilities = facilities

class Schedule:
    def __init__(self, employee, office, date, start_time, end_time):
        self.employee = employee
        self.office = office
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
