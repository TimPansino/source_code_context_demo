#!/bin/bash

newrelic-admin run-program gunicorn main:app -w 3 -t 120 >>/var/log/python.log 2>&1 &
locust --headless --users 3 --spawn-rate 1 -f /locustfile.py