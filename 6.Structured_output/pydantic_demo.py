from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class student(BaseModel):
    name : str 
    email : EmailStr
    age : Optional[int] = None
    cgpa : float = Field(gt=0,lt=10,default=6,description="decimal value representing the cgpa")


new_student = {'name':'pratik','age':20,'email':'pratik@gmail.com','cgpa':8}

Student = student(**new_student)
print(Student)

student_json = Student.model_dump_json()
print(student_json)