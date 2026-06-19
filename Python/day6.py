# List of Dictionaries

orders = [
    {"customer" : "Sadvik", "amount" : 10034},
    {"customer" : "Satyarth", "amount" : 5000},
    {"customer" : "Pratyush", "amount" : 3000},]

total = 0
# Adding Counters for each category
premium_count = 0      
vip_count = 0
regular_count = 0
for order in orders:

    amount = order["amount"]
    total += amount

    if amount >= 10000:
        category = "Premium"
        premium_count += 1
    elif amount >= 5000:
        category = "VIP"
        vip_count += 1
    else:
        category = "Regular"
        regular_count += 1

    print(f"Customer: {order['customer']}, Amount: {amount}, Category: {category}")

print("Total Order Value:" , total)

print("Premium Customers:", premium_count)
print("VIP Customers:", vip_count)
print("Regular Customers:", regular_count)

         


# print(orders)

# Accessing data 

# print(orders[0]) # first order
# print(orders[0]["amount"]) # amount of first order

# Loop through all orders

# for order in orders:
#  print(order["customer"], "-" , order["amount"])


orders =[
    {"customer" : "Sadvik" , "amount" : 11034},
    {"customer" : "Sakshi" , "amount" : 8970},
    {"customer" : "Prakash" , "amount" : 123456},
    
]

total = 0 
premium_count = 0
vip_count = 0
regular_count = 0 

for order in orders:
    amount = order["amount"]
    total += amount

    if amount >= 10000:
        category = "Premium"
        premium_count += 1 

    elif amount >= 5000:
        category = "VIP"
        vip_count += 1
    else:
        category = "Regular"
        regular_count += 1

    print(f"Customer : {order['customer']}, Amount : {amount}, Category : {category}")

print("Total Order Value:" , total)

print("Premium Customers:", premium_count)
print("VIP Customers:", vip_count)
print("Regular Customers:", regular_count)
