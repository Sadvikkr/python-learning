from fastapi import HTTPException

from app.data.students import students
from app.schemas.student import Student


def home():
    return {"message" : "Student API Running"}

    

def get_all_students(
        age: int = None, 
        name: str = None, 
        marks: int = None, 
        sort: str = None, 
        search: str = None, 
        page: int = 1, 
        limit: int = 10):
       

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




def get_student_by_id(id: int):
    
    for student in students:
        if student["id"] == id:
            return student
    raise HTTPException(
        status_code= 404,
        detail="Student Not Found"
    )
    

def create_student(student: Student):
    student_data = student.model_dump()  # student.dict() can also be used 
    next_id = len(students) + 1
    student_data["id"] = next_id

    
    students.append(student_data) 
  
    return {
        "message": "Student Created",
        "student": student_data
    }
       

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


def delete_student(id: int):
    
    for student in students:

        if student["id"] == id:
            students.remove(student)
            return {"message" : "Successfully deleted student"}

        
    return {
        "message" : "Student not found"
    }