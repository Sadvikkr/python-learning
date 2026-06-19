# Mini task DAY 02 - Student Profile System 

name = input("Enter student name : ")
marks = int(input("Enter marks: "))

if marks>=40:
  result = "Passed"
else:
  result = "Failed"
print("Student name:",name)
print("Marks:",marks)
print("Result:",result)

passed = marks>=40
print(passed)

