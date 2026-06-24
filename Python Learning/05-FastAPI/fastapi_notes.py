# FastAPI

# FastAPI is a Python framework used to build APIs.

# app = FastAPI()
# Creates a FastAPI application.

# @app.get("/")
# Creates a GET endpoint.

# @app.post("/")
# Creates a POST endpoint.

# @app.put("/")
# Creates a PUT endpoint.

# @app.delete("/")
# Creates a DELETE endpoint.

# FastAPI exposes Python functions as APIs.

# Example:

# @app.get("/students")
# def students():
#     return {"name": "Sadvik"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")   # When someone visits "/" Run the function below.

def home():   # Normal Python function.
    return {"message": "Backend is running"}

@app.get("/employee")
def employee():
    return {
        "name": "Sadvik",
        "salary": 50000
    }