#!/bin/bash

# Run pip install to install dependencies
pip install pipenv

pipenv install --dev

pipenv shell

# Apply migrations
python manage.py migrate

export DJANGO_SUPERUSER_USERNAME="$DJANGO_SUPERUSER_USERNAME"
export DJANGO_SUPERUSER_EMAIL="$DJANGO_SUPERUSER_EMAIL"
export DJANGO_SUPERUSER_PASSWORD="$DJANGO_SUPERUSER_PASSWORD"
# Create a superuser from env variables
python manage.py createsuperuser --noinput
