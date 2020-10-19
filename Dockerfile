FROM python:3.8 as dev

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y


WORKDIR /backend

RUN pip install --upgrade pip

# Add requirements file first, to cache dependencies
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt gunicorn

# Add source code
COPY . .

RUN export $(grep -v '^#' .env | xargs)

ENV DJANGO_SETTINGS_MODULE="app.settings" \
    PYTHONPATH=/backend

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", ":8000", "--reload", "app.wsgi"]

#CMD sh scripts/gunicorn.sh

