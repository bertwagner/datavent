# datavent
An event management application for programming conferences. 


# Build instructions


## Config
In the root project folder, remove the "-sample" suffix from the .env files. Update the variables in those files that have "CHANGEME" mentioned in them (ie. don't use the default secret keys, usernames, and passwords).

## Developing 

All requirements are managed within the docker containers. To run Django commands, do them within the Docker container. For example, to create a new registration app, start the container and execute the `startapp` command inside the container:

```
make dev
docker-compose exec web python manage.py startapp registration
```

Once Django creates the necessary file structures, you can stop the container:

`make stop`

## Testing

To run your dev container and view it locally, run `make dev`. The container should then be acecssible at http://localhost:8000.

## Deploying

To deploy the website to AWS, run:

```
make push-ecr-prod
make deploy-prod
make ssh
```

Once sshed into the server, run `infra/run.sh` to repull the images from AWS ECR and start the containers.

## References

[This article](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) was used as a starting point.
As well as [this article on Django](https://docs.djangoproject.com/en/4.2/intro/tutorial01/).