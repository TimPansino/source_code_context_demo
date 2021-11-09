import time
import random
from locust import HttpUser, task, between

class User(HttpUser):
    wait_time = between(60, 60*3)
    host="http://localhost:8000"

    @task(2)
    def simple(self):
        self.client.get("/")

    @task(1)
    def external(self):
        self.client.get("/external")

    @task(1)
    def simple_error(self):
        self.client.get("/error")

    @task(1)
    def external_error(self):
        self.client.get("/external/error")

    @task(1)
    def db_calls(self):
        self.client.get("/letters/%d" % random.randint(1, 35))
