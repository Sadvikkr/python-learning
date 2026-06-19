# Mini task DAY 05 - Customer Profile

# customer = {
#     "name" :"Sadvik",
#     "age" : 19 ,
#     "city" : "Hyderabad",
#     "premium_member" : True,
# }

# for key , value in customer.items():
#     print(key , ":" , value)


customer = input("Enter Customer Name : " )
age = int(input("Enter Customer Age :"))
city = input("Enter Customer City : ")

customer_profile = {
   "name" : customer,
   "age": age , 
   "city" : city, 
}

for key , value in customer_profile.items():
      print(key , ":" , value)

print(f"Hello {customer}, from {city}")   

# Even Odd check 

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Number Repeater 

number = int(input("Enter a number: "))
name = input("Enter a name: ")

for i in range(number):
    print(name)

# Order Analyzer

orders = []
 
for i in range(5):
   amount = float(input("Enter order amount : "))
   orders.append(amount) # add the amount to the list



# amount_1 = float(input("Enter order amount 1: "))
# amount_2 = float(input("Enter order amount 2: "))  
# amount_3 = float(input("Enter order amount 3: "))
# amount_4 = float(input("Enter order amount 4: "))
# amount_5 = float(input("Enter order amount 5: "))


print("Orders:", orders)

total = 0

for order in orders:
    total += order

    if order >= 10000:
        category = "Premium"
    elif order >= 5000:
        category = "VIP"
    else:
        category = "Regular"

    print(f"Order {order} : {category}")

print("Total Order Value:", total)

# # Student Result System 

name = input("Enter student name: ")
subject1 = float(input("Enter marks for Physics: "))
subject2 = float(input("Enter marks for Chemistry: "))  
subject3 = float(input("Enter marks for Mathematics: "))  

subjects = [subject1, subject2, subject3]

average = (subject1 + subject2 + subject3) / 3  # Or average = sum(subjects) / len(subjects)

if average >= 40:
    result = "Passed"
else:    result = "Failed"

print("Student Name:", name)
print("Marks:", subjects)
print("Average:", average)
print("Result:", result)

# OR 

name = input("Enter student name: ")
subject = []

for i in range(3):
    marks = float(input("Enter marks :"))
    subject.append(marks)
# subject1 = float(input("Enter marks for Physics: "))
# subject2 = float(input("Enter marks for Chemistry: "))  
# subject3 = float(input("Enter marks for Mathematics: "))  

subjects = subject

average = sum(subjects) / len(subjects)  # Or average = sum(subjects) / len(subjects)

if average >= 40:
    result = "Passed"
else:    result = "Failed"

print("Student Name:", name)
print("Marks:", subjects)
print("Average:", average)
print("Result:", result)