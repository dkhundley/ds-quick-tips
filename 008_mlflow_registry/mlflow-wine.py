# Importing in necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn

# Loading data and prepping for training
df_wine = pd.read_csv('../data/wine/train.csv')

X = df_wine.drop(columns = 'quality')
y = df_wine[['quality']]

X_train, X_val, y_train, y_val = train_test_split(X, y, random_state = 42)

# Defining model parameters
alpha = 1
l1_ratio = 2

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

    # Logging model to MLFlow
    mlflow.sklearn.log_model(model, 'model')
