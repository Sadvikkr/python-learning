order = {
    "customer": {
        "name": "Rahul"
    },
    "line_items": [
        {"product": "T-shirt", "price": 500},
        {"product": "Cap", "price": 200}
    ]
}

total = 0

if "line_items" in order and len(order["line_items"]) > 0:
    for item in order["line_items"]:
        total = total + item["price"]
else:
    total = 0

print(total)
