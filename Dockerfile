FROM python:3.8
LABEL maintainer="Chris Strutton <cstrutton@stackpole.ca><chris@rodandfly.ca>"

ENV APP = /app

RUN mkdir APP
WORKDIR APP

# Copy the uWSGI ini file to the current directory
COPY requirements.txt .

# Copy the requirements file in order to install
FROM python:3.8
LABEL maintainer="Chris Strutton <cstrutton@stackpole.ca><chris@rodandfly.ca>"

ENV APP = /app

RUN mkdir $APP
WORKDIR $APP

# Copy the requirements file in order to install
# Python dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt
# We copy the rest of the codebase into the image

COPY ./uwsgi.ini ./uwsgi.ini

COPY ./app .

EXPOSE 80

# Finally, we run uWSGI with the ini file we
# created earlier
CMD [ "uwsgi", "--ini", "uwsgi.ini" ]