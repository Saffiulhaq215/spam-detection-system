from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

# 1. Initialize the FastAPI app
app = FastAPI(title="Spam Detection API")

# 2. Load the Model and Vectorizer
# We do this outside the function so it only happens once when the server starts.
MODEL_PATH = "models/spam_model.pkl"
VECTORIZER_PATH = "models/vectorizer.pkl"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# 3. Define the Data Format (Pydantic)
# This ensures that whoever calls our API sends a "text" field.
class EmailRequest(BaseModel):
    message: str

# 4. Create the Prediction Endpoint
@app.post("/predict")
def predict_spam(request: EmailRequest):
    # a. Take the text from the request
    text = [request.message]
    
    # b. Convert the text into numbers using our saved vectorizer
    vectorized_text = vectorizer.transform(text)
    
    # c. Make the prediction (returns 0 or 1)
    prediction = model.predict(vectorized_text)[0]
    
    # d. Turn the 0/1 back into a readable word
    label = "Spam" if prediction == 1 else "Ham"
    
    return {
        "message_received": request.message,
        "prediction": label
    }

# 5. Root endpoint (just to check if the server is alive)
@app.get("/")
def home():
    return {"status": "The Spam Detector API is running!"}