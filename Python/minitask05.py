# Mini Task DAY 07 - Function Practice


# define function
#       ↓
# create marks list
#       ↓
# call function
#       ↓
# function runs calculation
#       ↓
# return result
#       ↓
# print result


# EX - 1

# def check_even_odd(number):

#     if number % 2 == 0:
#         return "Even"
#     else: 
#         return "Odd"
    
# result = check_even_odd(7)
# print(result)    


# EX - 2 

# def calculate_avg(marks):

#     average = sum(marks) / len(marks)
#     return average

# marks = [70, 80, 90]
# avg = calculate_avg(marks)
# print("Average Marks:", avg)


# EX - 3 - Student Result Function

# def check_result(marks):

#     average = sum(marks) / len(marks)

#     if average >= 40:
#         result = "Passed"
#     else:
#         result = "Failed"
#     return average, result
    
# marks = [70, 80, 90]
# avg, result = check_result(marks)
# print("Average Marks:", avg)
# print("Result:", result)    



# Date - 03 June 2026


# def greet(name):
#     print("Hello", name)

# greet("Sadvik")    


# def square(num):
#     return num*num

# result = square(5)
# print(result)

# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
          
# result = check_even_odd(8)
# print(result)

# def check_result(marks):

#     avg = sum(marks)/ len(marks)

#     if avg >= 40:
#         result = "Passed"
#     else:
#         result = "Failed"

#     return avg, result
# marks = [70, 90, 90]
# avg, result = check_result(marks)
# print("Average Marks:", avg)
# print("Result:", result)

# def classify_order(amount):

#     if amount >= 10000:
#         return "Premium"
    
#     elif amount >= 5000:
#         return "VIP"
#     else:
#         return "Regular"
    
# result = classify_order(12000)
# print(result)  



# def get_customer_category(age):

#     if age < 18 :
#         return "Minor"
#     elif age >= 60:
#         return "Senior Citizen"
#     else:
#         return "Adult"
    
# result = get_customer_category(6)
# print(result)    


# def calculate_total(expenses):

#     total = sum(expenses)
#     return total

# expenses = [500, 1000, 250]
# total_expenses = calculate_total(expenses)
# print("Total Expenses :" , total_expenses)

# def check_password(password):

#     if len(password) >= 8:
#         return "Valid"
#     else:
#         return "Invalid"
    
# result = check_password("Pass1234")
# print(result)    

#     # if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
#     #     return "Strong Password"
#     # else:
#     #     return "Weak Password"


# def check_result(marks):

#     avg = sum(marks) / len(marks)

#     if avg >= 90:
#         result = "Passed"
#         grade = "A+"

#     elif avg >= 80:
#         result = "Passed"
#         grade = "A"

#     elif avg >= 60:
#         result = "Passed"
#         grade = "B"

#     elif avg >= 40:
#         result = "Passed"
#         grade = "C"     

#     else: 
#         result = "Failed"
#         grade = "F"

#     return avg, result, grade

# marks = [80, 90, 85]
# avg, result, grade = check_result(marks)
# print("Average Marks:" , avg)           
# print("Result:", result)
# print("Grade:", grade)

def classify_orders(order_amounts):  # order_amounts is a list of order values and we need orders( many ) ,, so we need to run the loop . previously we need order ( one ) so if/elif/else are sufficient 
    premium_count = 0
    vip_count = 0
    regular_count = 0

    for amount in order_amounts:
        if amount >= 10000:
           premium_count += 1
        elif amount >= 5000:
            vip_count += 1
        else:
            regular_count += 1

    return premium_count, vip_count, regular_count    

order_amounts = [12000, 7000, 3000, 15000]
premium, vip, regular = classify_orders(order_amounts)
print("Premium Orders:", premium)
print("VIP Orders:", vip)
print("Regular Orders:", regular)