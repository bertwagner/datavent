dev:
	docker-compose up --build

prod:
	docker-compose -f docker-compose.prod.yml up --build -d
	docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
	docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

stop:
	docker-compose down -v --remove-orphans
