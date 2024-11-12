act: act
	source .venv/bin/activate

run:
	python manage.py runserver

migration:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate