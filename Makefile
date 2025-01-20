CONTAINER := wingz_backend

.PHONY: run 
run:
	python wingz/manage.py runserver 0.0.0.0:9090

.PHONY: test
test:
	python wingz/manage.py test app

.PHONY: lint
lint:
	black .


.PHONY: seed
seed:
	docker-compose run --rm --no-deps $(CONTAINER) \
		python manage.py seed


.PHONY: shell
shell:
	docker-compose run --rm --no-deps $(CONTAINER) \
		python manage.py shell