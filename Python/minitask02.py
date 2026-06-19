# Mint task DAY 03 - Order Classification System 

name = input("Enter customer name: ")
amount = float(input("Enter order amount: "))

# Customer classification
if amount >= 10000:
    customer_type = "Premium"
    priority = "Express Priority"
elif amount >= 5000:        
    customer_type = "VIP"
    priority = "High Priority"
else: 
    customer_type = "Regular"
    priority = "Normal Priority"

print("Customer:", name)
print("Order Amount:", amount)
print("Customer Type:", customer_type)
print("Priority:", priority) 