from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    marks: int

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Student API Running"}

@app.get("/students")
def get_students():
    return[
        {"id": 1, "name": "Sadvik", "marks": 89},
        {"id": 2, "name": "Aditya", "marks": 78}
    ]

@app.get("/students/{id}")
def get_student(id: int):
    return{
        "id": id,
        "name": "Sadvik",
        "marks": 89
    }

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student Created",
        "student": student
    }