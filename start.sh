#!/bin/bash

# Run pip install to install dependencies
pip install pipenv

pipenv shell

pipenv install

python manage.py collectstatic --no-input
