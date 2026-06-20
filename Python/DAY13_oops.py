class Employee:
        
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def show_details(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

    def check_salary(self):

        if self.salary >= 50000:
            print("High Salary")

        else:
            print("Normal Salary")

e1 = Employee("Sadvik", 60000)

e1.show_details()
e1.check_salary()               