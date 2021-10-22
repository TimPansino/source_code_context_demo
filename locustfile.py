import time
from locust import HttpUser, task, between

class User(HttpUser):
    wait_time = between(60, 60*3)
    host="http://localhost:8000"

    @task(5)
    def hello_world(self):
        self.client.get("/")

    @task(1)
    def error(self):
        self.client.get("/error")