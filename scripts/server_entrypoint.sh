#!/bin/sh

# wait for postgres to become available before running migrations

sleep 3

python3 ./manage.py migrate --noinput

exec "$@"