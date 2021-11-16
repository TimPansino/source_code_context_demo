#!/bin/bash

# Tee logs so application logs show up in stdout as well as logfile
newrelic-admin run-program gunicorn main:app -b 0.0.0.0:8000 -w 3 -t 120 | tee -a ./logs/python.log 2>&1 &

# Redirect logs without tee to remove spam from traffic driver
locust --headless --users 5 --spawn-rate 1 -f locustfile.py >>./logs/locust.log 2>&1
