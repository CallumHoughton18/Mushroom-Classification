FROM python:3.7.5-slim-buster

MAINTAINER Callum Houghton "Callum.Houghton13@hotmail.co.uk"

WORKDIR /app

# Prevents .pyc files written to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevrnts buffering of stdout and stderror
ENV PYTHONUNBUFFERED 1

COPY ./src /app

RUN ls /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt