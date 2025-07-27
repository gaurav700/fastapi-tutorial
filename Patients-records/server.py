from fastapi import FastAPI, Path, Query, HTTPException
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
    return {"message": "Welcome to the home page"}




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



## sort patients by weight, height, bmi, age
@app.get("/sort")
def sortPatients(sort_by : str = Query(..., description="The parameter by which you want to sort the patients", example="weight"), 
sort_order : str = Query('asc', description="The order in which you want to sort the patients", examples="asc/desc")):
    data = load_data()
    valid_fields = ["weight", "height", "bmi", "age"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Sort field not found in {valid_fields}')

    if sort_order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort order. Use 'asc' or 'desc'.")

    sorted_order = True if sort_order == 'desc' else False
    sorted_data = sorted(data.items(), key=lambda x: x[1][sort_by], reverse=sorted_order)
    return sorted_data



