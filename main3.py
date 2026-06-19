from fastapi import FastAPI, HTTPException

app = FastAPI()

def calculate_total(order):
    try:
        items = order["line_items"]
    except:
        return None

    if len(items) == 0:
        return 0

    total = 0
    for item in items:
        try:
            total += item["price"]
        except:
            continue

    return total


@app.get("/")
def home():
    return {"message": "Backend running"}


@app.post("/calculate")
def calculate(order: dict):
    total = calculate_total(order)

    if total is None:
        raise HTTPException(status_code=400, detail="line_items missing")

    return {"total": total}
