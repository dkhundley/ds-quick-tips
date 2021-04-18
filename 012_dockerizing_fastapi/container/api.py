import pandas as pd
import pickle
from fastapi import FastAPI

# Instantiating FastAPI
api = FastAPI()

# Loading in model from serialized .pkl file
pkl_filename = "../model/iris_model.pkl"
with open(pkl_filename, 'rb') as file:
	lr_model = pickle.load(file)

# Defining a test root path and message
@api.get('/')
def root():
	return {'message': 'Hello friends!'}