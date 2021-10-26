#!/bin/bash

newrelic-admin run-program gunicorn main:app -w 3 -t 120 >>/var/log/python.log 2>&1 &
locust --headless --users 5 --spawn-rate 1 -f locustfile.py >>/var/log/locust.log 2>&1
