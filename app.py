from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import pickle

# Load the model using pickle
with open('cnn_lstm__smote_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the input schema
class PredictionInput(BaseModel):
    data: list  # Input features as a list of floats

# Create FastAPI instance
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CNN-LSTM API is running!"}

@app.post("/predict/")
def predict(input_data: PredictionInput):
    try:
        # Preprocess input data
        input_array = np.array(input_data.data).reshape(1, -1, 1)  # Reshape for model input

        # Perform prediction
        prediction = model.predict(input_array)
        is_malicious = int(prediction[0] > 0.5)  # 0 for benign, 1 for malicious

        return {
            "prediction": "malicious" if is_malicious else "benign",
            "confidence": float(prediction[0])  # Confidence score
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
