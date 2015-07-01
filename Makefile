help:
	@echo 'dev          - installs dev requirements and sets up dev environment'
	@echo 'help         - shows this help message'
	@echo 'prod         - install prod requirements and sets up prod environment'
	@echo 'run          - runs the server'
	@echo 'superuser    - creates a superuser'
	@echo 'sync         - syncs and migrates the database'

dev:
	@echo "from settings.development import *" > src/settings/local.py
	venv/bin/pip install -r src/requirements/dev.txt --upgrade

prod:
	@echo "from settings.production import *" > src/settings/local.py
	venv/bin/pip install -r src/requirements/prod.txt --upgrade
	venv/bin/python src/manage.py collectstatic --noinput

run:
	venv/bin/python src/manage.py runserver $(shell ifconfig eth0 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1' | awk '{print $1}'):5555

sync:
	venv/bin/python src/manage.py syncdb --noinput
	venv/bin/python src/manage.py migrate

superuser:
	venv/bin/python src/manage.py createsuperuser

.PHONY: dev prod run superuser sync