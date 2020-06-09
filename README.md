### Setup for Dev: ###

Clone the Repo
```
git clone https://cstrutton@bitbucket.org/cstrutton/gfx-viewer.git
```

Create the virtual env
```
cd gfx-viewer
python3 -m venv venv
```

Install the requirements
```
cd src
pip install -r reqirments.txt
```

Start the dev server with hot reloading
```
cd app
FLASK_APP=app.py FLASK_ENV=development flask run
```

## Update Production image to latest version ##

```
on the server:
docker-compose down
git pull origin master
docker-compose build
docker-compose up -d
```
