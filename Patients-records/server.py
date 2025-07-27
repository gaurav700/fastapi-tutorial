from fastapi import FastAPI
app = FastAPI()
import json


# utitlity function to load json data
def load_data():
    with open("patients.json", 'r') as f:
        data = json.load(f)
    return data



# Home page
@app.get("/")
def home():
    return "Welcome to the home page"



# getting all the patients
@app.get("/view")
def viewPatients():
    data = load_data()
    return data


# getting patient information with his id
@app.get("/view/{patient_id}")
def viewPatientsWithId(patient_id : str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]


