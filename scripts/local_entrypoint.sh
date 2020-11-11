#!/bin/sh

cd /code

/bin/sh -c "python3 ./manage.py migrate"

/bin/sh -c "python3 ./manage.py runserver 127.0.0.1:8000"