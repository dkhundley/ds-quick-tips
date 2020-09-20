from locust import HttpUser, task, between
import json

with open('test_data/test_1.json') as f:
    test_data = json.loads(f.read())

class APIUser(HttpUser):
    host = 'http://localhost:5001'
    wait_time = between(3, 5)

    @task()
    def predict_endpoint(self):
        self.client.post('/predict', json = test_data)
