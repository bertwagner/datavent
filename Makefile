dev:
	docker-compose up --build

prod:
	docker-compose -f docker-compose.prod.yml up --build -d
	docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
	docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

stop:
	docker-compose down -v --remove-orphans

push-ecr-staging:
	docker-compose -f docker-compose.staging.yml build  
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 756669507085.dkr.ecr.us-east-1.amazonaws.com
	docker-compose -f docker-compose.staging.yml push

push-ecr-prod:
	docker-compose -f docker-compose.prod.yml build  
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 756669507085.dkr.ecr.us-east-1.amazonaws.com
	docker-compose -f docker-compose.prod.yml push

deploy-staging:
	scp -i ~/.ssh/neodata.dev.pem -r $(pwd)/{app,nginx,.env.staging,.env.staging.db,.env.staging.proxy-companion,docker-compose.staging.yml} admin@52.204.136.74:~/neodata

deploy-prod:
	scp -i ~/.ssh/neodata.dev.pem -r $(pwd)/{app,nginx,.env.prod,.env.prod.db,.env.prod.proxy-companion,docker-compose.prod.yml} admin@52.204.136.74:~/neodata
