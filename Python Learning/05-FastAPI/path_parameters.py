# PATH PARAMETERS

# Path parameters allow data to be passed through the URL.

# Example:
from fastapi import FastAPI

app = FastAPI()

@app.get("/employees/{id}")
def get_employee(id):
    return {"employee_id": id}

# URL:
# /employees/25

# FastAPI automatically stores:
# id = 25

# Output:
# {"employee_id": 25}

# Examples:

# /students/1
# /students/2
# /students/3

# /orders/5001
# /orders/5002

# Path parameters make dynamic URLs possible.

 
# ----------------
# ----------------

# Type Validation 

@app.get("/students/{id}")
def get_student(id: int):
    return {"student_id": id}   # id must be integer otherwise function will not run

