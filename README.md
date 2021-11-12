# Source Code Context Demo

This demo is meant to provide a proof of concept as well as example data for the experimental source code context for the New Relic Python Agent.

## Usage (Docker)

### Requirements

* Docker
* docker-compose (shipped with Docker desktop for Mac)
* GNU Make (Optional, for scripting shortcuts)
* New Relic license key set in environment variable (`export NEW_RELIC_LICENSE_KEY=mylicensekey`)
* Port 8000 available (port can also be changed in compose file, eg. `127.0.0.1:9999:8000` for port `9999`)

### Instructions

1. Build and start the application with `make up` or `docker-compose up -d --build`.
1. View logs for various components in the generated `logs/` directory.
1. Stop the application `make down` or `docker-compose down`.

## Development (Local)

### Requirements

* Python
* Python virtual_env package (if on Python 2)
* New Relic license key set in environment variable (`export NEW_RELIC_LICENSE_KEY=mylicensekey`)
* Port 8000 available (port can also be changed in compose file, eg. `127.0.0.1:9999:8000` for port `9999`)

### Instructions

1. Create a virtual environment with `python -m virtualenv .venv`.
1. Activate the new virtual environment with `source .venv/bin/activate` (for bash).
1. Install requirments with `pip install -r requirements.txt`.
1. Navigate to `src/` with `cd src`.
1. Start the application with `newrelic-admin run-program gunicorn main:app -w 3 -t 120`.
1. Optionally start the traffic driver from another terminal with `cd src` and `locust --headless --users 5 --spawn-rate 1 -f locustfile.py`
1. View logs in the `src/logs/` directory.
1. Stop the application with `Ctrl-C`.

Note: In order to configure the agent to send context attributes, add `source_code_context.enabled=True` to the newrelic.ini file. This setting currently defaults to False and if it is not explicitly added to the agent configuration file, no attributes will be attached to any data type.
