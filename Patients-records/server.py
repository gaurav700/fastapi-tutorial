from fastapi import FastAPI, Path
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
def viewPatientsWithId(patient_id : str = Path(..., description="The id of the patient you want to view", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {
        "error" : "Patient not found with id " + patient_id
        }



