from pydantic import BaseModel, Field

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
