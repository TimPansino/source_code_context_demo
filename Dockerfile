FROM ubuntu:latest

# Install OS packages
RUN apt-get update && \
    apt-get -y install python3 python3-pip git curl && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Init log files
RUN touch /var/log/cron.log
RUN touch /var/log/python.log

# Add source code
COPY newrelic.ini /newrelic.ini
COPY main.py /main.py
COPY locustfile.py /locustfile.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set env vars
ENV NEW_RELIC_CONFIG_FILE=/newrelic.ini

# Start with script
ENTRYPOINT [ "/entrypoint.sh" ]
