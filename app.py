#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI 
from pydantic import BaseModel 
import joblib # type: ignore
import numpy as np
import uvicorn

class InputData(BaseModel):
    Married : float
    ApplicantIncome : float
    Education : float
    LoanAmount : float
    Credit_History : float
   
scaler = joblib.load("Scaler.pkl")
model = joblib.load("model.pkl")
    
app = FastAPI()
    
@app.post("/predict/")
def predict(input_data : InputData):
    x_values = np.array([[
        input_data.Married,
        input_data.ApplicantIncome,
        input_data.Education,
        input_data.LoanAmount,
        input_data.Credit_History
    ]])    
    
    scaled_x_values = scaler.transform(x_values)
        
    prediction = model.predict(scaled_x_values)
        
    prediction = int(prediction[0])
    
    return {"prediction": prediction}
    
    
if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port = 8080)



# Exemple the bank advisor enter number of the 5 features given by costumer, and thanks to FastAPI, 
# the result is Loan_Status : "1"
# Married =  0
# ApplicantIncome = 2500
# Education = 1
# LoanAmount = 100
# Credit_History = 1

#To see the app, in the terminal enter "uvicorn app:app --reload" and go to this web site : http://127.0.0.1:8000/docs