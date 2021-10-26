python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
sleep 2
#firefox http://localhost:8000/show
#
#chromium http://localhost:8000/show
#/usr/bin/x-www-browser --app=http://localhost:8000/show
/usr/bin/x-www-browser --incognito http://localhost:8000/show

