# Pull base image

FROM python:3.8

# Set environment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /br-main

COPY Pipfile Pipfile.lock /br-main/
RUN pip install pipenv && pipenv install --system

COPY . /br-main/
