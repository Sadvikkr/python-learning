# import json
# try:
#     with open("employee_record.json", "r") as file:
#         employees = json.load(file)
# except FileNotFoundError:
#      employees =[]

# name = input("Enter employee name: ")
# salary = float(input("Enter salary: "))

# new_record = {
#     "employee_name" : name,
#     "salary" : salary,

# }

# employees.append(new_record)

# with open("employee_record.json", "w") as file:
#     json.dump(employees, file, indent = 4)

# print("All employee records: ")

# for record in employees:
#     print("Employee:", record["employee_name"])
#     print("Salary:", record["salary"])


import json

def load_employees():

    try:
        with open("employee_record.json", "r") as file:
            employees = json.load(file)

    except FileNotFoundError:
        employees = []

    return employees 
         
def save_employees(employees):

    with open("employee_record.json", "w") as file:
        json.dump(employees, file, indent = 4)

def add_employees(employees, name, salary):

    new_employee = {
        "name" : name,
        "salary" : salary
    }          
    employees.append(new_employee)

def view_employees(employees):
    print("All employees list: ")
    for employee in employees:
        print(employee)

def search_employees(employees):

    search_employee = input("Enter Employee Name to search: ")
    found = False
    for employee in employees:
        
       

        if employee["name"] == search_employee:
            print(employee)

            found = True

    if not found: 
            print("Employee Not found")   

def delete_employees(employees):

    delete_employee = input("Enter Employee name to delete: ")
    found = False
    for employee in employees:

        if employee["name"] == delete_employee:
            employees.remove(employee)
            print(employee)

            found = True
    if not found:
           print("Employee Not found")





# employees = load_employees()
# name = input("Enter employee name: ")
# salary = float(input("Enter salary: "))
# add_employees(employees, name, salary)
# save_employees(employees)
# view_employees(employees)


while True:

    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")


    choice = input("Enter choice: ")

    if choice == "1":

           employees = load_employees()
           name = input("Enter Employee Name: ")
           salary = float(input("Enter salary: "))
           add_employees(employees, name, salary) 
           save_employees(employees)

    elif choice == "2":
         
        employees = load_employees()
        view_employees(employees)

    elif choice == "3":
         employees = load_employees()
         search_employees(employees)

    elif choice == "4":
        employees = load_employees()
        delete_employees(employees)
        save_employees(employees)

    elif choice == "5": 
        break

    else: 
        print("Invalid choice:")     
        