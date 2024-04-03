from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
from pymongo import MongoClient
from typing import Optional

# Load the pre-trained machine learning model for heart disease prediction
model = joblib.load("heart_disease_model.pkl")

# Create an instance of the FastAPI application
app = FastAPI()

# Connect to the MongoDB database
client = MongoClient("mongodb://localhost:27017/")  # Use the default connection if no explicit database is provided
db = client["heart_disease_db"]
collection = db["user_inputs"]

# Define a Pydantic model for the user input data
class HeartData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

# Route for predicting heart disease based on user input
@app.post("/predict/")
def predict_heart_disease(data: HeartData):
    try:
        # Convert the user input data to a list
        input_data = [data.age, data.sex, data.cp, data.trestbps, data.chol, data.fbs, data.restecg,
                      data.thalach, data.exang, data.oldpeak, data.slope, data.ca, data.thal]

        # Store the user input data in the MongoDB collection
        result = collection.insert_one({"input_data": input_data})

        # Make a prediction using the loaded machine learning model
        prediction = model.predict([input_data])[0]

        # Update the stored MongoDB document with the prediction result
        collection.update_one({"_id": result.inserted_id}, {"$set": {"prediction": int(prediction)}})

        return {"prediction": int(prediction)}

    except Exception as e:
        # Raise an HTTP exception with a 500 status code and the error message
        raise HTTPException(status_code=500, detail=str(e))

# Route for testing if the API is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Heart Disease Prediction System API"}

# Route for storing input data directly without making a prediction
@app.get("/store-input/")  # Changed route name for clarity
def store_input(age: int, sex: int, cp: int, trestbps: int, chol: int, fbs: int,
                restecg: int, thalach: int, exang: int, oldpeak: float,
                slope: int, ca: int, thal: int):
    try:
        # Create a dictionary to hold the input data
        input_data = {
            "age": age,
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs,
            "restecg": restecg,
            "thalach": thalach,
            "exang": exang,
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal
        }

        # Store the user input data in the MongoDB collection
        collection.insert_one({"input_data": input_data})

        return {"message": "Input data stored successfully"}
    except Exception as e:
        # Raise an HTTP exception with a 500 status code and the error message
        raise HTTPException(status_code=500, detail=str(e))