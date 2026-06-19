def get_customer_email(order):
    if "customer" in order and "email" in order["customer"]:
        return order["customer"]["email"]
    else:
        return None
