# revolt-backend
[![Build Status](https://travis-ci.org/Studentmediene/kapina-backend.svg?branch=dev)](https://travis-ci.org/Studentmediene/kapina-backend)
[![Test Coverage](https://api.codeclimate.com/v1/badges/00e9c6201d2821d81f79/test_coverage)](https://codeclimate.com/github/Studentmediene/kapina-backend/test_coverage)

Backend for radiorevolt.no

## Environment settings

Settings are read from environment variables.
By default settings are configured for development and should just work, but some changes are required in production. 

|Name|Default|Description|
|:---|:------|:----------|
|REVOLT_DEBUG|True|Enable Django debug. Set to false in production|
|REVOLT_ALLOWED_HOSTS|(Empty)|Hosts allowed to access webserver. e.g. 'radiorevolt.no'|
|DATABASE_URL|(BASE_DIR)/db.sqlite3|[See dj-database-url](https://github.com/kennethreitz/dj-database-url#url-schema)
|REVOLT_STATIC_ROOT|(BASE_DIR)/staticfiles|Folder where static files are located|
|REVOLT_MEDIA_ROOT|(BASE_DIR)/mediafiles|Files where uploaded media is located|
|REVOLT_SECRET_KEY|replace_this_secret_key|[See Django SECRET_KEY](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-SECRET_KEY). **It is important that this is changed in production.**
|REVOLT_RAVEN_DSN|(Empty)|Sentry DSN using this format: https://user:pass@sentry.io/project|


## Setup - Development

### Virtualenv

```bash
pip install virtualenv
virtualenv -p python3 venv
. venv/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
sudo apt-get install libpq-dev python3-dev
pip install psycopg2
```

### Change settings

The default settings provided should work fine for development, but if any changes are needed a tool like [direnv](https://direnv.net/) is recommended for handling environment variables. 

### Setup database and load data dump
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py loaddata chimera_import_script/data.json
```

### Start the development server
```bash
python manage.py runserver
```

### Testing and linting
We use `pytest`, `isort` and `flake8`  to test and lint the project.
Run the commands before commiting:
```bash
flake8 api_graphql app data_models
yapf -pir api_graphql app data_models -e '**/migrations' -e '**/snapshots'
isort -rc api_graphql app data_models
pytest

```

## Setup - Deployment

### Nginx

```bash
apt-get install nginx
```

Copy the nginx config (Updated as of 12/02/2017) to /etc/nginx/sites-available/radiorevolt.conf:
```
server {

  listen 80;
  # Type your domain name below
  server_name radiorevolt.no www.radiorevolt.no beta.radiorevolt.no;

  root /var/www;
  index index.html;
    
# Always serve index.html for any request
  location / {
    try_files $uri $uri/ /index.html;
    allow all;
  }
  location /static/ {
      alias   /var/www/static/;
  }
  
  location /media/ {
      alias   /var/www/media/;
  }
  location ~ /.well-known {
        allow all;
  }	
##
# If you want to use Node/Rails/etc. API server
# on the same port (443) config Nginx as a reverse proxy.
# For security reasons use a firewall like ufw in Ubuntu
# and deny port 3000/tcp.
##

   location /staging/api {
    proxy_pass http://localhost:9000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
  }

  location /graphql {
    proxy_pass http://localhost:8000/graphql;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
  }

  location /admin/ {
    proxy_pass http://localhost:8000/admin/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
  }

  location /graphiql {
    proxy_pass http://localhost:8000/graphiql;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
  }

  location /grappelli {
    proxy_pass http://localhost:8000/grappelli;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
  }

  location /summernote/ {
    proxy_pass http://localhost:8000/summernote/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
  }
}
```
Enable the config by creating a symlink in /etc/nginx/sites-enabled:
```bash
sudo ln -s /etc/nginx/sites-available/radiorevolt.conf /etc/nginx/sites-enabled/radiorevolt.conf
```

If the server is only listening to IPv6 addresses replace this line:
```
listen 80;
```
With this line:
```
listen [::]:80 default ipv6only=on;
```


### Clone repo

```bash
mkdir /webapps
cd /webapps
git clone https://github.com/Studentmediene/revolt-backend.git
```

### Install PostgreSQL

```
sudo apt-get install postgresql postgresql-contrib
su - postgres
createuser --interactive -P
```

```
Enter name of role to add: revolt-backend
Enter password for new role: **********
Enter it again: (Ask your closest project leader for this)
Shall the new role be a superuser? (y/n) n
Shall the new role be allowed to create databases? (y/n) n
Shall the new role be allowed to create more new roles? (y/n) n
```

```bash
createdb --owner revolt-backend radiorevolt
\q
exit
```

### Create an application user

```bash
groupadd --system webapps
useradd --system --gid webapps --shell /bin/bash --home /webapps/revolt-backend revoltbackend
chown -R revoltbackend: /webapps/revolt-backend
```

### Virtualenvironment

```bash
cd /webapps/revolt-backend/
sudo apt-get install python3-pip
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
sudo apt-get install libpq-dev python3-dev
pip install psycopg2
pip install gunicorn
pip install setproctitle
sudo apt-get install supervisor
```

Copy data dump:
```bash
sudo cp chimera_import_script/data.json /webapps/revolt-backend/
```


### Change settings

In production environment variables can be added to the supervisor/systemd service. See settings table at the top of the readme for full list.

Recommended changes:

```
REVOLT_DEBUG=false
REVOLT_ALLOWED_HOSTS="radiorevolt.no"
DATABASE_URL=postgres://revolt-backend:(password_here)@localhost/radiorevolt
REVOLT_STATIC_ROOT=/var/www/static/
REVOLT_MEDIA_ROOT=/var/www/media/
REVOLT_SECRET_KEY=(generate this with something like 'openssl rand -base64 32')
```

### Setup database and load data dump
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py loaddata data.json
```

### Setup Gunicorn
Copy the Gunicorn config to /webapps/revolt-backend/gunicorn_start:
```
#!/bin/bash

NAME="revolt-backend"                               # Name of the application
DJANGODIR=/webapps/revolt-backend                   # Django project directory
SOCKFILE=/webapps/revolt-backend/run/gunicorn.sock  # we will communicate using this unix socket
USER=revoltbackend                                  # the user to run as
GROUP=webapps                                       # the group to run as
NUM_WORKERS=3                                       # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=app.settings               # which settings file should Django use
DJANGO_WSGI_MODULE=app.wsgi                       # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
#  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
```
Make the file exectuable:
```bash
chmod +x /webapps/revolt-backend/gunicorn_start
```


### Setup Supervisor
Copy the Supervisor config to /etc/supervisor/conf.d/revolt-backend.conf:
```
[program:revolt-backend]
command =sh /webapps/revolt-backend/gunicorn_start
user = revoltbackend
stdout_logfile = /webapps/revolt-backend/logs/gunicorn_supervisor.log
redirect_stderr = true
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8
```

Add environment settings to the environment list.

Enable Supervisor:
```
sudo systemctl enable supervisor.service
```
Create log file and restart Supervisor:
```bash
mkdir -p /webapps/revolt-backend/logs/
touch /webapps/revolt-backend/logs/gunicorn_supervisor.log
supervisorctl reread
```

IF YOU GET AN ERROR (https://github.com/Supervisor/supervisor/issues/121):

```
service supervisor start
supervisorctl reload
supervisorctl update
```
