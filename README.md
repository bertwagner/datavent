# datavent
An event management application for programming conferences. 


# Build instructions


## Config
In the root project folder, remove the "-sample" suffix from the .env files. Update the variables in those files that have "CHANGEME" mentioned in them (ie. don't use the default secret keys, usernames, and passwords).

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