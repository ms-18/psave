#! /bin/sh

cd /code

/bin/sh -c "python3 ./manage.py migrate --noinput"

/bin/sh -c "python3 ./manage.py runserver 0.0.0.0:8000"

exec "$@"