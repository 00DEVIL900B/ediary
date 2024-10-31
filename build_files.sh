#!/bin/bash
echo "Building..."
python3 -m pip install -r requirements.txt
echo "Migrating..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
echo "Collecting..."
python3 manage.py collectstatic --noinput
