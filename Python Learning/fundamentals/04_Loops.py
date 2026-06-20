# Lists

# order1 = 2000
# order2 = 5000
# order3 = 9000 ( Wrong format for multiple orders )

# orders = [2000, 5000, 9000, 12000]  # Correct format for multiple orders

# # Accessing elements in the list

# prices = [100, 200, 300]

# print(prices[0]) # Output: 100
# print(prices[1]) # Output: 200
# print(prices[2]) # Output: 300

# prices[1] = 250  # Modifying an element in the list
# print(prices)  # Output: [100, 250, 300]

# # Adding new elements to the list
# prices.append(400) 
# print(prices) # Output: [100, 250, 300, 400]

# #Length of the list
# print(len(prices)) # Output: 4

# # Loops with lists
# orders = [2000, 5000, 9000, 12000]
# for order in orders:
#     print(order)





# Loops 
 
# for loop , This is used when we have multiple items.
# for i in range(5):
#     print(i)

# for i in range(1, 6):
#     print(i)

# for i in range(3):
#     print("Hello")    


# while loop , Used when repetition depends on condition.

# count = 1
# while count <= 5:
#     print(count)
#     count +=1

# TASK 1 

# for i in range(1,11):
#     print(i)



# for i in range(1,6):
#     print("Sadvik")




# numbers = [1,2,3,4,5,6,7,8]
# count = 0
# for n in numbers:
#     if n % 2 == 0:
#         count +=1
# print(count)




# while True:
#     num = int(input("Enter number: "))

#     if num == 0:
#         break






# while True:
#     age = int(input("Enter age: "))

    
#     if age <= 0:
#         print("Invalid age. Please enter a non-negative number.")
#         continue

#     if age > 0:
#         print(age)
#         break





# students = [
#     {"name": "Sadvik"},
#     {"name": "Ananya"},
#     {"name": "Rohan"}
# ]

# for student in students:
#     print(student["name"])


total = 0 
count = 0 # counters and accumulators must be OUTSIDE the loop
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    total += num
    count += 1
print("Total:", total)    
print("Count:", count)    


