# get Magazzino running

- `source .env/bin/activate`

- `cd lorenzoProject/`

- `./run.sh`

- point web browser to http://localhost:8000

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


# alternate DB
If MySQL support is unnecessary or unwanted, simplest way to store your data is SQlite
in `settings.py` alterate DATABASES object like this below:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
