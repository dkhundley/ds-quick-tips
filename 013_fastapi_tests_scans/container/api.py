import pandas as pd
import pickle
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


## API INSTANTIATION
## ----------------------------------------------------------------
# Instantiating FastAPI
api = FastAPI()

# Loading in model from serialized .pkl file
pkl_filename = "../models/iris_model.pkl"
with open(pkl_filename, 'rb') as file:
    lr_model = pickle.load(file)



## API ENDPOINTS
## ----------------------------------------------------------------
# Defining a test root path and message
@api.get('/')
def root():
    msg = {'message': 'Hello friends!'}
    return JSONResponse(content = msg, status_code = 200)



# Defining the prediction endpoint without data validation
@api.post('/predict')
async def predict(request: Request):

    # Getting the JSON from the body of the request
    input_data = await request.json()

    # Converting JSON to Pandas DataFrame
    input_df = pd.DataFrame([input_data])

    # Getting the prediction from the Logistic Regression model
    pred = lr_model.predict(input_df)[0]

    return JSONResponse(content = pred, status_code = 200)