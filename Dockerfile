# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-buster

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app"
COPY . /app/.
RUN mkdir /app/tmp

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 "main:create_app()"
