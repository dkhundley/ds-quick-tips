import pandas as pd
import joblib
from fastapi import FastAPI
import uvicorn
import json



## PRELOADED COMPONENTS
# ------------------------------------------------------------------------------
# Instantiating the Flask application
application = FastAPI(title = 'Red Wine FastAPI Model',
                      description = 'A FastAPI demo using a simple ElasticNet Regression model.',
                      docs_url = '/')

# Loading the saved, serialized model
model = joblib.load('model.pkl')



## API ENDPOINTS
# ------------------------------------------------------------------------------
# Defining our prediction endpoint
@application.post('/predict')
def predict(body: dict):
    # Transforming JSON data to DataFrame
    predict_df = pd.json_normalize(body)

    # Running data through model
    pred = model.predict(predict_df)[0]

    # Returning prediction to user
    return {'prediction': pred}

# Defining our health endpoint
@application.get('/health')
def health():
    return {'Status': 'Healthy!'}



if __name__ == '__main__':
    uvicorn.run("fastapi_api:application", host='0.0.0.0', port = 8000, workers = 4)
