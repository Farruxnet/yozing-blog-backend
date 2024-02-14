mig:
	python manage.py makemigrations
	python manage.py migrate
deploy:
	python manage.py collectstatic
	python manage.py createsuperuser
	python manage.py check
	python manage.py check --deploy
