### Setup to run on device with systemd ###

Clone and install the Repo:
```
cd /opt
sudo git clone https://cstrutton@bitbucket.org/cstrutton/gfx-viewer.git
cd gfx-viewer
pip3 install uwsgi # install seperate as it won't work in windows
pip3 install -r src/requirements.txt
```

Install the service:
```
sudo cp service_files/viewer.service /etc/systemd/system/viewer.service
sudo systemd enable viewer.service
sudo systemd daemon-reload
sudo systemd start viewer.service
```

Update:
```
cd /opt/gfx-viewer
sudo git pull
pip3 install -r src/requirements.txt
sudo cp service_files/viewer.service /etc/systemd/system/viewer.service
sudo systemd enable viewer.service
sudo systemd daemon-reload
sudo systemd restart viewer.service
```

View logs:
```
journalctrl -f -u viewer
```


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
docker-compose down
git pull origin master
docker-compose build
docker-compose up -d
```


