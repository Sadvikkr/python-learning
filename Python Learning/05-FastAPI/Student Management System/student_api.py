from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi import HTTPException
from pydantic import Field
from dotenv import load_dotenv  

import os

load_dotenv()

app = FastAPI()

class Student(BaseModel):   # to validate incoming data
    name: str
    age: int = Field(ge=0)
    marks: int = Field(ge=0, le=100)
    email: str
    password: str
    phone: str

class StudentResponse(BaseModel):  # to validate outgoing data 
    name: str
    age: int = Field(ge=0)
    marks: int = Field(ge=0, le=100)

students = [
    {
        "id": 1,
        "name": "Sadvik",
        "age": 19,
        "marks": 89,
        "email": "sadvikkk@gmail.com",
        "password": "123test@",
        "phone": "9897456378"
    },
    {
        "id": 2,
        "name": "Aman",
        "age": 20,
        "marks": 95,
        "email": "amankr@gmail.com",
        "password": "87653wh",
        "phone": "7623568987"
    },
    {
        "id": 3,
        "name": "Ayush",
        "age": 19,
        "marks": 76,
        "email": "ayush@gmai.com",
        "password": "ayu6754",
        "phone": "9967511125"
    },
    {
        "id": 4,
        "name": "Aman",
        "age": 19,
        "marks": 90,
        "email": "aman@gmail.com",
        "password": "123456",
        "phone": "9876543210"
}

]


# def get_db():
#     return "Database Connection"

def get_current_user():
    return {
        "name": "Sadvik",
        "role": "Admin"
    }


@app.get("/")
def home():
    return {"message" : "Student API Running"}

    
@app.get("/students", response_model = list[StudentResponse])
def get_students(user = Depends(get_current_user), age: int = None, name: str = None, marks: int = None, sort: str = None, search: str = None, page: int = 1, limit: int = 10):
        print(user)

        filtered_students = students

        temp = []

        if age is not None:
        
            for student in filtered_students:
                if age == student["age"]:
                   temp.append(student)
            filtered_students = temp

        temp = []
        if name is not None:
            for student in filtered_students:
                if student["name"] == name:
                   temp.append(student)
            filtered_students = temp

        temp = []

        if marks is not None:
            for student in filtered_students:
                if student["marks"] == marks:
                    temp.append(student)
            filtered_students = temp   

        temp =[]
        if search is not None:
            for student in filtered_students:
                if search.lower() in student["name"].lower() :
                    temp.append(student)
            filtered_students = temp    
        
         
        if sort is not None:
            allowed_fields = ["id", "name", "age", "marks"]
            if sort in allowed_fields:
                sorted_students = sorted(filtered_students, key = lambda student : student[sort]  , reverse = False)
                filtered_students = sorted_students
            else:
                return {"message": "Invalid sort field"}
        

        start = ( page - 1) * limit
        end = start + limit 
        filtered_students = filtered_students[start:end]
                         


        return filtered_students



@app.get("/students/{id}")
def get_student(id: int):
    
    for student in students:
        if student["id"] == id:
            return student
    raise HTTPException(
        status_code= 404,
        detail="Student Not Found"
    )
    
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
       

@app.put("/students/{id}")
def update_student(id : int, student: Student):  #What information does the backend need to complete this task?
    student_data = student.model_dump()
    
    for student in students:
        
         if student["id"] == id:
                student["name"] = student_data["name"]
                student["age"] = student_data["age"]
                student["marks"] = student_data["marks"]
                
                return student
        
    return {
        "message": "Student not found"
        }

@app.delete("/students/{id}")
def delete_student(id: int):
    
    for student in students:

        if student["id"] == id:
            students.remove(student)
            return {"message" : "Successfully deleted student"}

        
    return {
        "message" : "Student not found"
    }





           

    
        


    