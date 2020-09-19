import pandas as pd
import joblib
from flask import Flask, request, json, Response, jsonify, make_response
from helpers import create_embarked_columns, create_age_bins


## PRELOADED COMPONENTS
# ------------------------------------------------------------------------------

# Instantiating the Flask application
application = Flask(__name__)

# Loading the saved, serialized model
model = joblib.load('../model/rfc_pipeline.pkl')

## API ENDPOINTS
# ------------------------------------------------------------------------------

# Defining our prediction endpoint
@application.route('/predict', methods = ['POST'])
def predict():

    # Getting incoming data from request
    predict_json = request.json

    # Transforming JSON data to DataFrame
    predict_df = pd.json_normalize(predict_json)

    # Running data through model
    preds = model.predict(predict_df)

    # Prepping preds to be returned to user
    js = json.dumps({'preds': str(preds[0])})

    return Response(js, status = 200, mimetype = 'application/json')



# Defining a basic health endpoint
@application.route('/health', methods = ['GET'])
def health():

    # Dumping out simple health message
    js = json.dumps({'Status': 'Healthy!'})

    return Response(js, status = 200, mimetype = 'application/json')


## SCRIPT INVOCATION
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    # Starting the Flask API on script invocation
    application.run(host = '0.0.0.0', debug = True)
