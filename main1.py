from fastapi import FastAPI

app = FastAPI()

def calculate_total(order):
    total = 0
    for item in order["line_items"]:
        total += item["price"]
    return total


@app.get("/")
def home():
    return {"message": "Backend running"}


@app.post("/calculate")
def calculate(order: dict):
    total = calculate_total(order)
    return {"total": total}
