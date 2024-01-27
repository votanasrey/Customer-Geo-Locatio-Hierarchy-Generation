FROM python:3.9-slim

WORKDIR /code
COPY . /code

RUN pip3 install --no-cache-dir -r /code/requirements.txt
