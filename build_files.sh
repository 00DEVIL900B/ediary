#!/bin/bash
python 3.9 manage.py migrate
python 3.9 manage.py collectstatic --noinput
python 3.9 manage.py runserver 0.0.0.0:$PORT
