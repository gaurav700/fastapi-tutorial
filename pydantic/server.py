# Data validation in python without pydantic
# def insert_patient_data(name: str, age : int):
#     if type(name) == str and type(age) == int:
#         if age<0:
#             raise ValueError('age cannot be negative')
#         else:
#             print(name)
#             print(age)
#     else:
#         raise TypeError('name and age must be string and int respectively')


# insert_patient_data('John',20)
# insert_patient_data(20,'John')
# insert_patient_data('John','20')


# Data validation with pydantic
from pydantic import BaseModel, ValidationError

# Taking info from user
name = input("Enter name : ")
age = input("Enter age : ")
PATIENT_INFO = { "name" : name, "age" : age } 

# Creating pydantic base model
class Patient(BaseModel):
    name: str
    age: int

# Defining function
def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)

# calling function
patient1 = Patient(**PATIENT_INFO)
insert_patient_data(patient1)

