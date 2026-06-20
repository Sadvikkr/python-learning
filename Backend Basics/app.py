# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Backend running"}

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/greet")

# def greet(name: str):
#     return {"message": f"Hello, {name}!"}

# @app.get("/check")
# def check_number(num: int):

#     if num % 2 == 0:
#         return {"result": "Even"}
#     else:
#         return {"result": "Odd"}

# import json

# @app.get("/machine")
# def machine_usage(machine: str, start: int, stop: int):

#     if stop < start:
#         return {"error": "Stop time cannot be less than start time"}

#     usage = stop - start

#     record = {
#         "machine": machine,
#         "start": start,
#         "stop": stop,
#         "usage": usage
#     }

#     try:
#         with open("machine_usage.json", "r") as file:
#             data = json.load(file)
#             if isinstance(data, dict):
#                 data = [data]
#     except:
#         data = []

#     data.append(record)

#     with open("machine_usage.json", "w") as file:
#         json.dump(data, file, indent=4)

#     return {
#         "message": "Data saved",
#         "usage": f"{usage} hours"
#     }


# Converting to POST API

from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# Data model
class MachineInput(BaseModel):
    machine: str
    start: int
    stop: int

@app.post("/machine")
def machine_usage(data: MachineInput):

    if data.stop < data.start:
        return {"error": "Stop time cannot be less than start time"}

    usage = data.stop - data.start

    record = {
        "machine": data.machine,
        "start": data.start,
        "stop": data.stop,
        "usage": usage
    }

    try:
        with open("machine_usage.json", "r") as file:
            old_data = json.load(file)
            if isinstance(old_data, dict):
                old_data = [old_data]
    except:
        old_data = []

    old_data.append(record)

    with open("machine_usage.json", "w") as file:
        json.dump(old_data, file, indent=4)

    return {
        "message": "Saved successfully",
        "usage": f"{usage} hours"
    }