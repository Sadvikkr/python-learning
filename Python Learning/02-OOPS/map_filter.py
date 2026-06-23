# map() function - Transform Data 
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x*2 , numbers))
print(result)

# filter() function - Keep only matching data 

numbers = [1,2,3,4,5,6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

