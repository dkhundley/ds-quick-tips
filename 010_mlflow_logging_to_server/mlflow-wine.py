# Importing in necessary libraries
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn



# PROJECT SETUP
# ------------------------------------------------------------------------------
# Setting the MLflow tracking server
mlflow.set_tracking_uri('http://mlflow-server.local')

# Setting the requried environment variables
os.environ['MLFLOW_S3_ENDPOINT_URL'] = 'http://mlflow-minio.local/'
os.environ['AWS_ACCESS_KEY_ID'] = 'minio'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'minio123'

# Loading data from a CSV file
df_wine = pd.read_csv('../data/wine/train.csv')

# Separating the target class ('quality') from remainder of the training data
X = df_wine.drop(columns = 'quality')
y = df_wine[['quality']]

# Splitting the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, random_state = 42)




# MODEL TRAINING AND LOGGING
# ------------------------------------------------------------------------------
# Defining model parameters
alpha = 1
l1_ratio = 1

# Running MLFlow script
with mlflow.start_run():

    # Instantiating model with model parameters
    model = ElasticNet(alpha = alpha,
                       l1_ratio = l1_ratio)

    # Fitting training data to the model
    model.fit(X_train, y_train)

    # Running prediction on validation dataset
    preds = model.predict(X_val)

    # Getting metrics on the validation dataset
    rmse = mean_squared_error(preds, y_val)
    abs_error = mean_absolute_error(preds, y_val)
    r2 = r2_score(preds, y_val)

    # Logging params and metrics to MLFlow
    mlflow.log_param('alpha', alpha)
    mlflow.log_param('l1_ratio', l1_ratio)
    mlflow.log_metric('rmse', rmse)
    mlflow.log_metric('abs_error', abs_error)
    mlflow.log_metric('r2', r2)

    # Logging training data
    mlflow.log_artifact(local_path = '../data/wine/train.csv')

    # Logging training code
    mlflow.log_artifact(local_path = './mlflow-wine.py')

    # Logging model to MLFlow
    mlflow.sklearn.log_model(sk_model = model,
                             artifact_path = 'wine-pyfile-model',
                             registered_model_name = 'wine-pyfile-model')
