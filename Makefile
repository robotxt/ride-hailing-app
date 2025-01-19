.PHONY: run 
run:
	python wingz/manage.py runserver 0.0.0.0:9090

.PHONY: test
test:
	python wingz/manage.py test app

.PHONY: lint
lint:
	black .