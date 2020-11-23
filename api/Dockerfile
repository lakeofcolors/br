# Pull base image

FROM python:3.8

# Set environment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_DEBUG 1

WORKDIR /br-main

ENV PYTHONPATH "${PYTONPATH}:/br-main"

COPY Pipfile Pipfile.lock /br-main/
RUN pip install pipenv && pipenv install --system

COPY . /br-main/
