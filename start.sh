#!/usr/bin/env bash
# exit on error
set -o errexit

pip install pipenv

export PIPENV_YES=1

pipenv shell
pipenv install
python manage.py collectstatic --no-input