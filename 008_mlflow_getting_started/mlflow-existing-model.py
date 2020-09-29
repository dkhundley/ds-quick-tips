# Importing in necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn
import joblib

# Loading serialized model
model = joblib.load('model/model.pkl')

# Logging model to MLFlow
mlflow.sklearn.log_model(model, 'model')
