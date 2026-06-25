from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    marks: int

app = FastAPI()

students = [
    {
        "id": 1,
        "name": "Sadvik",
        "age": 19,
        "marks": 89
    },
    {
        "id": 2,
        "name": "Aman",
        "age": 20,
        "marks": 95
    }
]

@app.get("/")
def home():
    return {"message" : "Student API Running"}

@app.get("/students")
def get_students():
    return students
    

@app.get("/students/{id}")
def get_student(id: int):
    
    for student in students:
        if student["id"] == id:
            return student
          
@app.post("/students")
def create_student(student: Student):
    student_data = student.model_dump()  # student.dict() can also be used 
    next_id = len(students) + 1
    student_data["id"] = next_id

    
    students.append(student_data)   
    return {
        "message": "Student Created",
        "student": student_data
    }

    