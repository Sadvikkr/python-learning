# Error Handling

# try:
#     age = int(input("Enter age: "))
#     print("Age is:", age)
# except ValueError:
#     print("Invalid input")

# try:
#     result = 10 / 0

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# EX - 2
# try:
#     num = int(input("Enter a number: "))
#     print(num*2)
# except ValueError:
#     print("Please enter a valid number")




# numbers = []

# while len(numbers) < 3:
#      try:
#          num = int(input("Enter number: "))
#          numbers.append(num)  # add the number to the list
#      except ValueError:
#          print("Invalid input, try again")
# print("Numbers:", numbers)

# average = sum(numbers) / len(numbers)
# print("Average:", average)


# 0 to stop the loop
# total = 0
# while True:
#     try:
#         num = int(input("Enter number (0 to stop): "))

#     except ValueError:
#         print("Invalid input, try again")
#         continue

#     if num == 0:
#         break

#     print("You entered:", num)  

#     total += num
# print("Total:", total)




# try:
#     num = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num / num2
#     print("Result:", result)
# except ValueError:
#     print("Invalid input, please enter a number") 
# except ZeroDivisionError:
#     print("Cannot divide by zero")       





while True:
    try:
        age = int(input("Enter age: "))
        break
    except ValueError:
        print("Invalid input")