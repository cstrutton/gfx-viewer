FROM python:3.8

LABEL maintainer="Chris Strutton <cstrutton@stackpole.ca><chris@rodandfly.ca>"

ENV TZ America/Toronto

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install uWSGI seperately as it does not install in windows
RUN pip install uwsgi

# copy and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

COPY . /usr/src/app

EXPOSE 80


