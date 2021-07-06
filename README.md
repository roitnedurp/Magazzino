# get Magazzino running

- `source .env/bin/activate`

- `cd lorenzoProject/`

- `./run.sh`

# requirements
- django
- django-widget-tweaks
- mysqlclient
- libmariadb-dev (debian package)

# creating a virtualenv
- `cd lorenzoProject/`
- `python3 -m venv .env`
- `source .env/bin/activate`
- `pip install django`
- `pip install django-widget-tweaks`
- `sudo apt update && sudo apt install libmariadb-dev`
- `pip install mysqlclient`
