line_items = [
    {"product": "T-shirt", "vendor": "A", "price": 500},
    {"product": "Cap", "vendor": "A", "price": 200}
]

total = 0

for item in line_items:
    total = total + item["price"]

print(total);
