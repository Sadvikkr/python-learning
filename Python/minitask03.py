# Mini task DAY 04 - Total Order Calculator

orders = [2000, 5000, 7000, 12000]

total = 0  # We need storage or initial value to store the total amount

for order in orders:
    total = total + order # or total += order

    if order >= 10000:
        category = "Premium"
    elif order >= 5000:
        category = "VIP"
    else:
          category = "Regular"

    print("Order", order, "-" , category)
    

print("Total Order Value :", total)