# Dockerfile

# pull the official docker image
FROM python:3.13-rc-slim

# set work directory
WORKDIR /fastapi_app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
WORKDIR /
COPY . /fastapi_app