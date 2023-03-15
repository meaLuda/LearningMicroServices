FROM python:3.10.9-slim-bullseye

WORKDIR /cast_services

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .