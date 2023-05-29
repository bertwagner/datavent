# Read in variables form a .env file
ifneq (,$(wildcard ./.env.prod))
    include .env.prod
    export
endif

dev:
	docker-compose up --build

prod:
	docker-compose -f docker-compose.prod.yml up --build -d
	docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
	docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

stop:
	docker-compose down -v --remove-orphans

push-ecr-staging:
	docker-compose -f docker-compose.staging.yml --env-file .env.staging build  
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${ECR_URI_BASE}
	docker-compose -f docker-compose.staging.yml push

push-ecr-prod:
	docker-compose -f docker-compose.prod.yml --env-file .env.prod build  
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${ECR_URI_BASE}
	docker-compose -f docker-compose.prod.yml push

deploy-staging:
	scp -i ~/.ssh/neodata.dev.pem -r app admin@${ELASTIC_IP}:~/neodata
	scp -i ~/.ssh/neodata.dev.pem -r nginx admin@${ELASTIC_IP}:~/neodata
	scp -i ~/.ssh/neodata.dev.pem -r .env.staging admin@${ELASTIC_IP}:~/neodata
	scp -i ~/.ssh/neodata.dev.pem -r .env.staging.db admin@${ELASTIC_IP}:~/neodata
	scp -i ~/.ssh/neodata.dev.pem -r .env.staging.proxy-companion admin@${ELASTIC_IP}:~/neodata
	scp -i ~/.ssh/neodata.dev.pem -r docker-compose.staging.yml admin@${ELASTIC_IP}:~/neodata
	
deploy-prod:
	scp -i ~/.ssh/neodata.dev.pem -r app admin@${ELASTIC_IP}:~/neodata
	scp -i ~/.ssh/neodata.dev.pem -r nginx admin@${ELASTIC_IP}:~/neodata
	scp -i ~/.ssh/neodata.dev.pem -r .env.prod admin@${ELASTIC_IP}:~/neodata
	scp -i ~/.ssh/neodata.dev.pem -r .env.prod.db admin@${ELASTIC_IP}:~/neodata
	scp -i ~/.ssh/neodata.dev.pem -r .env.prod.proxy-companion admin@${ELASTIC_IP}:~/neodata
	scp -i ~/.ssh/neodata.dev.pem -r docker-compose.prod.yml admin@${ELASTIC_IP}:~/neodata

wtf:
	echo "hi"