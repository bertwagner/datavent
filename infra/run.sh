#!/bin/bash

source .env.prod


docker-compose -f docker-compose.prod.yml --env-file .env.prod down -v --remove-orphans

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ECR_URI_BASE
docker pull $ECR_URI:web
docker pull $ECR_URI:nginx-proxy

docker-compose -f docker-compose.prod.yml --env-file .env.prod up -d
