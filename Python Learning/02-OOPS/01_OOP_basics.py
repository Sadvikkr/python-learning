# OOPS 


# Class = Blueprint
# Object = Actual Thing
# self = This Object
# Attributes = Data stored inside object
# Method = Function inside class

class Student:
    
    def __init__(self, name, marks): #__init__ is a special method that runs automatically when an object is created and is used to initialize the object's data.
        self.name = name 
        self.marks = marks

    def show_details(self):
        print("Name:" , self.name)
        print("Marks:" , self.marks)

    def check_result(self):  
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")      


# s1 = Student("Sadvik", 85)

# s1.show_details()
# s1.check_result()

    def update_marks(self, new_marks):
        self.marks = new_marks

s1 = Student("Sadvik", 85)
# s1.show_details()
s1.update_marks(100)
# s1.show_details()
print(s1.name, s1.marks )

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("Sadvik", 85)

# print(s1.name)
# print(s1.marks)

# s1.marks = 100

# print(s1.marks)