# Conditions (Decision Making)
"Basic syntax" 
# if condition:
    # action

age = int(input("Enter age: "))

if age >= 18:
    print("Adult")

#If-else

marks = 30

if marks >= 40:
    print("Passed")
else:
    print("Failed")

# elif (Multiple Decisions)

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")        # Execution is from top to bottom , Stops when condition becomes True.


# Logical Operators

age = int(input("Enter age : "))
paid = input("Has the payment been made? (yes/no): ")

if age>= 18 and paid == "yes":
    print("Access Granted")
else: 
    print("Access Denied")

