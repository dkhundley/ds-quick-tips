import json
from fastapi.testclient import TestClient
from container.api import api



## PYTEST SETUP
## --------------------------------------------------------------------------------------------------------------------
# Instantiating the test client from our container's API
client = TestClient(api)

# Loading test JSON file
with open('test_json/test_data.json', 'rb') as file:
    test_json = json.load(file)



## UNIT TEST CASES
## --------------------------------------------------------------------------------------------------------------------
# Creating a unit test for the basic root path
def test_root_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello friend!'}

# Creating a unit test for the prediction endpoint
def test_predict():
    response = client.post('/predict', json = test_json)
    assert response.status_code == 200