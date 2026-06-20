# INHERITANCE

# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

# class Student(Person):
#     pass

# s1 = Student("Sadvik", 20)

# print(s1.name)
# print(s1.age)



# EXAMPLE 2

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

class Student(Person):

    def __init__(self, name, age, marks):
        super().__init__(name, age) #Call the parent's constructor and let it initialize the parent's attributes.
        self.marks = marks
s1 = Student("Sadvik", 20, 97)

print(s1.name)
print(s1.age)
print(s1.marks)


# ENCAPSULATION - Don't let random code directly change important data.