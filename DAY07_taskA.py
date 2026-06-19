order = {
    "customer": {
        "name": "Sadvik",
        "email": "sadvik@gmail.com"
    },
    "line_items": [
        {"product": "T-shirt", "price": 200},
        {"product": "Cap", "price": 200}
    ]
}

def calculate_total(order):
    try:
        items = order["line_items"]
    except:
        return 0

    if len(items) == 0:
        return 0

    total = 0
    for item in items:
        try:
            total = total + item["price"]
        except:
            total = total + 0

    return total
def get_customer_email(order):
    try:
        return order["customer"]["email"]
    except:
        return None
def is_vip_order(total):
    if total >= 500:
        return "vip"
    else:
        return "regular"
def order_summary(total, email):
    # returns a dictionary
    return {
        "total": total,
        "email": email
    }
    


total = calculate_total(order)
email = get_customer_email(order)
vip = is_vip_order(total)
order_sum = order_summary(total, email)

print("Total:", total)
print("Email:", email)
print("VIP Order:", vip)
print("Order Summary:", order_sum)