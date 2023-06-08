
import requests
response = requests.get("http://localhost:8000")

def update_marks(employee_list): #ממיית את העובדים של אותו יום לפי צוותים ולפי הימים שעבדו בשבוע שעבר ומחזירה רשימה ממויינת
    for employee in employee_list: 
        employee['mark']=0
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

    requests.get("http://localhost:8000/sced_arr/1").json().employee_list[day_of_week].append(employee)

def update_lists(array_of_lists):
    for i in range(len(array_of_lists)):
        updated_list = update_marks(array_of_lists[i])
        array_of_lists[i] = updated_list

    DAL.sced_arr.update_schedule(array_of_lists)

    for i in range(len(array_of_lists)):
        process_lists(array_of_lists[i],i)
        


def process_lists(array_of_lists,day): #שולחת כל יום מהשבוע לפונקציה שתתנהג עם הנתונים בהתאם
    for lst in array_of_lists:
        list_size = len(lst)
        list_remainder = list_size % 50

        if list_size <= 250 and list_size >10 and list_remainder >= 10:
            confirmation(lst,day)
        elif list_size < 10:
            break
        elif list_size <= 250 and list_size >10 and list_remainder < 10:
            lst=filtering(lst)
            confirmation(lst,day)

def filtering(lst):
    remainder = len(lst) % 50
    new_list = lst[:-remainder]
    return new_list

def confirmation(employee_list, day_of_week):
    # Import the list of employees from the DAL layer
    dal_employee_list = requests.get("http://localhost:8000/employee/all").json()

    # Initialize the running variable
    running_variable = 0

    # Iterate through the list of employees
    for employee in employee_list:
        # Get the employee ID
        employee_id = employee['id']

        # Search for the employee in the DAL employee list using the ID
        dal_employee = next((emp for emp in dal_employee_list if emp['id'] == employee_id), None)

        if dal_employee:
            emp=requests.get("http://localhost:8000/employee/"+str(employee_id)).json()
            # Calculate the floor number based on the running variable
            emp.floor[day_of_week] = (running_variable // 50) + 1
            emp.home_work-=1
            DAL.employee.update(emp)
            # Increment the running variable
        running_variable += 1
    if(day_of_week==4):
         arr=requests.get("http://localhost:8000/sced_arr").json()
         for i in range(len(arr)):
            arr[i] = []
            DAL.sced_arr.update(arr)
    

    
