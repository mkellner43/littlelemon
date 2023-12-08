#!/usr/bin/env bash
# exit on error
set -o errexit

pip install pipenv

pipenv install
python manage.py collectstatic --no-input