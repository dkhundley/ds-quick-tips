from locust import HttpUser, task, between
import json

# Loading the test JSON data
with open('test.json') as f:
    test_data = json.loads(f.read())

# Creating an API User class inheriting from Locust's HttpUser class
class APIUser(HttpUser):
    # Setting the host name and wait_time
    host = 'http://localhost:8000'
    wait_time = between(7, 9)

    # Defining the post task using the JSON test data
    @task()
    def predict_endpoint(self):
        self.client.post('/predict', json = test_data)
