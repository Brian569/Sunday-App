serve:
	python3 manage.py runserver

shell:
	python3 manage.py shell

migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate
	