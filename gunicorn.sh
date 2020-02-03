#!/bin/bash

NAME="kapina-backend"                               	# Name of the application
DJANGODIR=/webapps/kapina-backend                   	# Django project directory
NUM_WORKERS=3                                       	# how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=app.settings                     # which settings file should Django use
DJANGO_WSGI_MODULE=app.wsgi                             # WSGI module name

echo "Starting $NAME as `whoami`"

cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start your Django Unicorn
exec venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --bind=127.0.0.1:8000 --bind [::1]:8000 \
  --log-level=debug \
  --log-file=/var/log/gunicorn/gunicorn.log