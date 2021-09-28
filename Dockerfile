FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create directory for the app user
RUN mkdir /apps

WORKDIR /apps

COPY req.txt /apps
COPY . /apps/

RUN pip install -r req.txt
