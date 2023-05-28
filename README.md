# datavent
An event management application for programming conferences. 


# Build instructions


## Config
In the root project folder, create the following 3 files. Update SECRET_KEY, SQL_USER, and SQL_PASSWORD values:

.env.dev:
```
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=datavent
SQL_USER=admin
SQL_PASSWORD=abc123
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

.env.prod:
```
DEBUG=0
SECRET_KEY=change_me
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=datavent_prod
SQL_USER=admin
SQL_PASSWORD=abc123
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

.env.prod.db
```
POSTGRES_USER=admin
POSTGRES_PASSWORD=abc123
POSTGRES_DB=datavent_prod
```

## Start containers
Dev:
`make dev`

Prod:
`make prod`

Stop: 
`make stop`

Then navigate to http://localhost:8000 (dev) or http://localhost:1337 (prod)

[This article](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) was used as a starting point.
As well as [this article on Django](https://docs.djangoproject.com/en/4.2/intro/tutorial01/).