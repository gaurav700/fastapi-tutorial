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
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Taking info from user

name = input("Enter name: ")

email = input("Enter email : ")

website = input("Enter website url : ")

age = input("Enter age: ")

weight = input("Enter weight: ")

allergies = []
while True:
    more = input("Do you want to enter allergies? (yes/no): ").strip().lower()
    if more == 'yes':
        allergies.append(input(f"Enter another allergy: "))
    elif more == 'no':
        break
    else:
        print("Please enter 'yes' or 'no'.")

contact = {}
print("Enter 2 contact details:")
for i in range(2):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for {key}: ")
    contact[key] = value
while True:
    more = input("Do you want to enter more contact details? (yes/no): ").strip().lower()
    if more == 'yes':
        key = input("Enter new contact key: ")
        value = input(f"Enter value for {key}: ")
        contact[key] = value
    elif more == 'no':
        break
    else:
        print("Please enter 'yes' or 'no'.")



PATIENT_INFO = { 
    "name" : name, 
    "age" : age,
    "email" : email,
    "website" : website,
    "weight" : weight,
    "allergies" : allergies,
    "contact" : contact
} 

# Creating pydantic base model
class Patient(BaseModel):
    name: Annotated(str, Field(max_length=50, title="Name of patient", description="Name of patient in less than 50 characters", example="John Doe"))
    age: int = Field(ge = 16, le=90)
    email : EmailStr
    website : AnyUrl
    weight : Annotated[float, Field(ge = 0, le=300, strict=True)] # true will only pass if it is a float
    allergies : Optional[List[str]] = None
    contact : Dict[str,str]

# Defining function
def insert_patient_data(patient : Patient):
    print("Name : " + patient.name)
    print("Age : " + str(patient.age))
    print("Email : "+ str(patient.email))
    print("Website : " + str(patient.website))
    print("Weight : " + str(patient.weight))
    print("Allergies : " + patient.allergies)
    print("Contact : " + patient.contact)

# calling function
patient1 = Patient(**PATIENT_INFO)
insert_patient_data(patient1)

