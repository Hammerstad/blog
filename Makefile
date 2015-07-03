help:
	@echo 'help         - shows this help message'
	@echo 'dev          - installs dev requirements and sets up dev environment'
	@echo 'prod         - install prod requirements and sets up prod environment'
	@echo 'run          - runs the server'
	@echo 'superuser    - creates a superuser'
	@echo 'sync         - syncs and migrates the database'
	@echo 'test         - runs all the tests for a given app. Example:'
	@echo '               make test app=app.blog'
	@echo 'coverage     - creates code coverage for a given app. Example:'
	@echo '               make coverage app=app.blog'

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
	
test:
	venv/bin/python src/manage.py test ${app}
	
coverage:
	coverage run --source='src' src/manage.py test ${app}

.PHONY: dev prod run superuser sync test coverage