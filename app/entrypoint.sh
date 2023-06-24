#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi

# python manage.py flush --no-input
# python manage.py migrate

export SQL_DATABASE=$SQL_DATABASE
export SQL_HOST=$SQL_HOST
export SQL_USER=$SQL_USER
export SQL_PASSWORD=$SQL_PASSWORD
export SQL_PORT=$SQL_PORT

exec "$@"
