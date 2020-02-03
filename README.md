# kapina-backend
[![Build Status](https://travis-ci.org/Studentmediene/kapina-backend.svg?branch=dev)](https://travis-ci.org/Studentmediene/kapina-backend)
[![Test Coverage](https://api.codeclimate.com/v1/badges/00e9c6201d2821d81f79/test_coverage)](https://codeclimate.com/github/Studentmediene/kapina-backend/test_coverage)

Backend for [RadioRevolt.no](https://radiorevolt.no)

## Setup - Development

### Virtualenv
Create a virtual environment for Python:

```bash
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

### Install requirements

```bash
sudo apt-get install libpq-dev python3-dev zlib1g-dev libjpeg-dev 
pip install -r requirements.txt
```

### Setup database and load data dump
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py loaddata data_models/fixtures/beta_fixtures.json
```

### Start the development server
```bash
python manage.py runserver
```

### Testing and linting
We use `pytest`, `isort`, `yapf` and `flake8`  to test and lint the project.
Run the commands before commiting:
```bash
flake8 api_graphql app data_models
yapf -pir api_graphql app data_models -e '**/migrations' -e '**/snapshots'
isort -rc api_graphql app data_models
pytest
```

## Git conventions
Can be found [here](https://confluence.smint.no/display/IT/Git+conventions).

## Deployment
Is described [here](https://confluence.smint.no/display/IT/Deployment).

## kapina-frontend
Can be found [here](https://github.com/Studentmediene/kapina-frontend)