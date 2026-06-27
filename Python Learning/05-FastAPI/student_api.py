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
    },
    {
        "id": 3,
        "name": "Aman",
        "age": 19,
        "marks": 76
    }
]

@app.get("/")
def home():
    return {"message" : "Student API Running"}

# @app.get("/students")
# def get_students():
#     return students
    
@app.get("/students")
def get_students(age: int = None, name: str = None, marks: int = None, sort: str = None, search: str = None, page: int = 1, limit: int = 10):
        
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


        # filtered_students = []
        # if age is None and name is None and marks is None: # None
        #    return students

        # elif age is not None and name is None and marks is None:  # age

        #     for student in students:
        #         if student["age"] == age:
        #             filtered_students.append(student)
        #     return filtered_students 

        # elif age is None and name is not None and marks is None:  # name 

        #     for student in students:
        #         if student["name"] == name:
        #             filtered_students.append(student)
        #     return filtered_students 

        # elif age is None and name is None and marks is not None: # marks

        #     for student in students:
        #         if student["marks"] == marks:
        #             filtered_students.append(student)
        #     return filtered_students

        # elif age is not None and name is not None and marks is None: # name , age    or age , name 
        #     for student in students:
        #         if student["name"] == name and student["age"] == age:
        #             filtered_students.append(student)
        #     return filtered_students 

        # elif age is not None and name is None and marks is not None: # marks , age    or age , marks
        #     for student in students:
        #         if student["marks"] == marks and student["age"] == age:
        #             filtered_students.append(student)
        #     return filtered_students 
        
        # elif age is None and name is not None and marks is not None: # marks , name     or name , marks
        #     for student in students:
        #         if student["marks"] == marks and student["name"] == name:
        #             filtered_students.append(student)
        #     return filtered_students 
        
        # elif age is not None and name is not None and marks is not None: # age , marks , name 
        #     for student in students:
        #         if student["marks"] == marks and student["name"] == name and student["age"] == age:
        #             filtered_students.append(student)
        #     return filtered_students
        
        









        # filtered_students = []
        # if age is None and name is None:
        #     return students
        
        # elif name is None and age is not None:  #Here student["age"] == age will not be applicable because student variable is not there , variables created inside a loop exist after the loop starts
           
        #     for student in students:
        #       if student["age"] == age:
        #         filtered_students.append(student)
        #     return filtered_students # outside the loop

        # elif name is not None and age is None:
            
        #     for student in students:
        #      if student["name"] == name:
        #         filtered_students.append(student)
        #     return filtered_students            

        # elif age is not None and name is not None:
        #     for student in students:
        #         if student["name"] == name and student["age"] == age:
        #             filtered_students.append(student)
        #     return filtered_students        

        # sorted(students, key = student["marks"], reverse = False)  
        # new_students = sorted(students)
        # return new_students


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
        
           

    
        


    