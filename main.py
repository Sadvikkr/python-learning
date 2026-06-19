# from fastapi import FastAPI

# app = FastAPI()

# def calculate_total(order):
#     total = 0
#     for item in order["line_items"]:
#         total += item["price"]
#     return total

# sample_order = {
#     "line_items": [
#         {"price": 500},
#         {"price": 200}
#     ]
# }

# @app.get("/")
# def home():
#     total = calculate_total(sample_order)
#     return {"total": total}

