class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Sadvik", 500000)    
e2 = Employee("Aman", 700000)


e1.salary = 600000

print(e1.name)
print(e1.salary)