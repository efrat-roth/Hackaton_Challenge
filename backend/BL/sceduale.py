import requests
response = requests.get("http://localhost:8000/employee/all")

def find_employee(username, password): # פונקציה שמקבלת שם משתמש וסיסמא ומחזירה את העובד המתאים
    employees = employee_dal. get_all_employees()
    for employee in employees:
        if employee.username == username and employee.password== password:
            return employee

    raise Exception("Employee not exist")  # זריקת חריגה אם העובד לא נמצא


def update_marks(employee_list): #ממיית את העובדים של אותו יום לפי צוותים ולפי הימים שעבדו בשבוע שעבר ומחזירה רשימה ממויינת
    for employee in employee_list: 
        employee['mark'] +=  employee['home_work']
# Count employees in each team
    team_counters = {}
    for employee in employee_list:
        team = employee['group']
        team_counters[team] = team_counters.get(team, 0) + 1

    # Sort the team counters array by team size (descending) and group number (ascending)
    sorted_teams = sorted(team_counters.items(), key=lambda x: (-x[1], x[0]))

    # Adjust marks based on team size
    for i, (team, count) in enumerate(sorted_teams, start=1):
        adjustment = 20 - (i - 1) * 3
        for employee in employee_list:
            if employee['group'] == team:
                employee['mark'] += adjustment 
    sorted_employees = sorted(employee_list, key=lambda x: x['mark'])
    return sorted_employees

def add_employee_to_list(day_of_week, employee):# מוסיפה ללוז הלא ממויין עובד
    if day_of_week < 0 or day_of_week > 4:
        raise ValueError("Invalid day of the week. Expected a number from 0 to 4.")

    # Access the array in the data layer and add the employee to the corresponding list

    DAL.sced_arr.get_schedule[day_of_week].add(employee)

def update_lists(array_of_lists):
    for i in range(len(array_of_lists)):
        updated_list = update(array_of_lists[i])
        array_of_lists[i] = updated_list

    DAL.sced_arr.update_schedule(array_of_lists)


def process_lists(array_of_lists): #שולחת כל יום מהשבוע לפונקציה שתתנהג עם הנתונים בהתאם
    for lst in array_of_lists:
        list_size = len(lst)
        list_remainder = list_size % 50

        if list_size <= 250 and list_size >10 and list_remainder >= 10:
            confirmation(lst)
        elif list_size < 10:
            break
        elif list_size <= 250 and list_size >10 and list_remainder < 10:
            lst=filtering(lst)
            confirmation(lst)

def filtering(lst):
    remainder = len(lst) % 50
    new_list = lst[:-remainder]
    return new_list

def confirmation(employee_list, day_of_week):
    # Import the list of employees from the DAL layer
    dal_employee_list = DAL.employee.GetAll()

    # Initialize the running variable
    running_variable = 0

    # Iterate through the list of employees
    for employee in employee_list:
        # Get the employee ID
        employee_id = employee['id']

        # Search for the employee in the DAL employee list using the ID
        dal_employee = next((emp for emp in dal_employee_list if emp['id'] == employee_id), None)

        if dal_employee:
            emp=DAL.employee.GetById(employee_id)
            # Calculate the floor number based on the running variable
            emp.floor[day_of_week] = (running_variable // 50) + 1
            emp.home_work-=1
            DAL.employee.update(emp)
            # Increment the running variable
        running_variable += 1


    
