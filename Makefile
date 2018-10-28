help:
	@echo '-------------Makefile for Animeinfo Api---------------'
	@echo '                                                      '
	@echo 'Usage:                                                '
	@echo '------> run         Run project                       '
	@echo '------> shell       Shell command line                '
	@echo '------> test        Run tests                         '
	@echo '------> createuser  Create superuser                  '
	@echo '------> setup       Setup the project                 '

run:
	python3 manage.py runserver

createuser:
	python3 manage.py createsuperuser

shell:
	python3 manage.py shell

test:
	python3 manage.py test -n

setup:
	pip install -r requirements.txt
	cd contrib/ python contrib/env_gen.py
	python3 manage.py makemigrations
	python3 manage.py migrate
