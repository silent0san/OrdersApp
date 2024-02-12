FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN apt-get update

COPY ./requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
