# Usual method 
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num * num)

print(squares)

# List Comprehension Method 

ssquares = [num*num for num in numbers]
print(squares)

# EX - 1

names = ["sadvik", "aman", "rahul"]

upper_names = [name.upper() for name in names]

print(upper_names)

# EX - 2


numbers = [1, 2, 3, 4]

result = [num + 10 for num in numbers]

print(result)


#  List Comprehension with conditions

# Normal Way 
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []

for num in numbers:

    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# List Comprehension Method 

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# # EX - 1 ( Names longer than 5 letters) 

names = ["Sadvik", "Aman", "Rahul", "Krishna"]
result = [name for name in names if len(name) > 5]
print(result)


# EX - 2 
numbers = [1, 2, 3, 4]

result = [num * 2 for num in numbers if num > 2]

print(result)
