#  Find largest number 

# def find_largest(a, b):

#     if a > b:
#         return a
#     else:
#         return b 
    
# result = find_largest(10, 25)
# print(result)

# Calculate discounts

# def calculate_discount(amount):
#     if amount >= 10000:
#         discount = amount *10/100  # or 0.1
#     else: 
#         discount = 0
#     return amount - discount

# result = calculate_discount(12000)
# print(result)

# Count Even numbers 

# def count_even(numbers):

#     count = 0
#     for num in numbers:
#         if num % 2 == 0:
#             count +=1

#     return count 
# numbers = [1, 2, 3, 4, 5, 6]
# result = count_even(numbers)    
# print(result)    

# Student Attendance Checker 

# def is_eligible(attendance):
#     if attendance >= 75:
#         return "Eligible"
#     else:
#         return "Not Eligible"
    
# result = is_eligible(80)
# print(result)

# Product Stock Checker

# def check_stock(stock):

#     if stock >10:
#         return "In Stock"
#     elif stock >0 and stock <=10:
#         return "Low Stock"
#     else:
#         return "Out of Stock"
    
# result = check_stock(5)
# print(result)    

# Find Avg Temperature

# def avg_temp(temps):

#     avg = sum(temps) / len(temps)
#     return avg

# temps = [30, 35, 40]
# result = avg_temp(temps)
# print(result)    

# Analyze Orders

# def analyze_orders(order_amounts):
#     total_orders = len(order_amounts)
#     total_revenue = sum(order_amounts)
#     average = total_revenue / len(order_amounts)
#     return total_orders, total_revenue, average

# order_amounts = [1000, 7000, 3000, 15000]
# total_orders, total_revenue, average = analyze_orders(order_amounts)
# print("Total Orders:", total_orders)
# print("Total Revenue:", total_revenue)
# print("Average Order Value:", average)

# Employee Salary Report

# def salary_report(salaires):

#     highest_salary = max(salaires)
#     lowest_salary = min(salaires)
#     avg_salary = sum(salaires) / len(salaires)
#     return highest_salary, lowest_salary, avg_salary

# salaires = [25000, 30000, 50000]
# highest_salary, lowest_salary, avg_salary = salary_report(salaires)
# print("Highest Salary:", highest_salary)
# print("Lowest Salary:", lowest_salary)
# print("Average Salary:", avg_salary)

# def check_pass(marks):
#     if marks >= 40:
#         return "Pass"
#     else:
#         return "Fail"

# result = check_pass(35)

# print(result)