from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class LineItem(BaseModel):
    price: float

class Order(BaseModel):
    line_items: List[LineItem]


@app.get("/")
def home():
    return {"message": "Backend running"}


@app.post("/calculate")
def calculate(order: Order):
    total = 0
    for item in order.line_items:
        total += item.price
    return {"total": total}
