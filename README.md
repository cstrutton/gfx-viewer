### Setup for Dev: ###

# clone repo
git clone https://cstrutton@bitbucket.org/cstrutton/gfx-viewer.git
# create venv
cd gfx-viewer
python3 -m venv venv

# install requirements
cd src
pip install -r reqirments.txt

# start the dev server
cd app
FLASK_APP=app.py FLASK_ENV=development flask run


### Update Production to latest version ###

on the server:
docker-compose down
git pull origin master
docker-compose build
docker-compose up -d

