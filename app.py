from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from schemas.patient_info import Patient, PatientUpdate
from utils.utils import save_data, load_data
import ast

app = FastAPI()

@app.get("/")
def get_start():
    return {"Message":"Hello World"}

@app.post("/data")
def user_data(value : Patient):
    data = load_data()
    data.append(value.model_dump())
    save_data(data)
    return JSONResponse(status_code=201, content="Succesfully added")

@app.put("/update/{name}")
def update_info(name: str, new_data :PatientUpdate):
    data = load_data()
    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    # Convert update to dict and exclude unset fields
    data_to_update = new_data.model_dump(exclude_unset=True)
    
    updated = False
    for index, item in enumerate(data):
        if item['name'] == name:
            for key, value in data_to_update.items():
                item[key] = value
            patient = Patient(**item)
            data[index] = patient.model_dump()
            updated = True
            break

    if not updated:
        raise HTTPException(status_code=404, detail=f"Patient with name {name} not found")  

    save_data(data)

    return {"data":f"{data}"}
    
    
    