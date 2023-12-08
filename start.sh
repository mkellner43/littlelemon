#!/usr/bin/env bash
# exit on error
set -o errexit

# Run pip install to install dependencies
pip install pipenv && pipenv shell && pipenv install && python manage.py collectstatic --no-input
