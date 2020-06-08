###Setup for Dev:###

clone repo

create venv

cd src
pip install -r reqirments-dev.txt

cd app
FLASK_APP=app.py FLASK_ENV=development flask run

###Update to Production###

on the server:
docker-compose down
git pull origin master
docker-compose build
docker-compose up -d

