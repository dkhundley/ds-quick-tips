import pandas as pd
import pickle
from fastapi import FastAPI, Request
from pydantic import BaseModel



## API INSTANTIATION
## ----------------------------------------------------------------

# Instantiating FastAPI
api = FastAPI()

# Loading in model from serialized .pkl file
pkl_filename = "../model/iris_model.pkl"
with open(pkl_filename, 'rb') as file:
	lr_model = pickle.load(file)

# Creating the data model for data validation
class Iris(BaseModel):
	sepal_length: float
	sepal_width: float
	petal_length: float
	petal_width: float
	
	
	
## API ENDPOINTS
## ----------------------------------------------------------------

# Defining a test root path and message
@api.get('/')
def root():
	return {'message': 'Hello friends!'}
	
	
	
# Defining the prediction endpoint without data validation
@api.post('/basic_predict')
async def basic_predict(request: Request):
	
	# Getting the JSON from the body of the request
	input_data = await request.json()
	
	# Converting JSON to Pandas DataFrame
	input_df = pd.DataFrame([input_data])
	
	# Getting the prediction from the Logistic Regression model
	pred = lr_model.predict(input_df)[0]
	
	return pred
	
	
	
# Defining the prediction endpoint with data validation
@api.post('/predict')
async def predict(iris: Iris):
	
	# Converting input data into Pandas DataFrame
	input_df = pd.DataFrame([iris.dict()])
	
	# Getting the prediction from the Logistic Regression model
	pred = lr_model.predict(input_df)[0]
	
	return pred