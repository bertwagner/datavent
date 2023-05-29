#!/bin/bash

docker-compose -f docker-compose.prod.yml --env-file .env.prod up --build -d
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear