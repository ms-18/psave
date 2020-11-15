#!/bin/sh

# wait for postgres to become available before running migrations

while ! (test -e $PGDATA/pg-init-done); do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done


# once postgres is up, sleep for a few seconds to give it time to fully initialize
sleep 3

su app -s /bin/sh -c "python3 ./manage.py migrate --noinput"

exec "@"