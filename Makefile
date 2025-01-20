CONTAINER := wingz_backend

.PHONY: run 
run:
	docker-compose up

.PHONY: test
test:
	docker-compose run --rm --no-deps $(CONTAINER) \
		python manage.py test app 

.PHONY: lint
lint:
	docker-compose run --rm --no-deps $(CONTAINER) \
		black .

.PHONY: seed
seed:
	docker-compose run --rm --no-deps $(CONTAINER) \
		python manage.py seed


.PHONY: shell
shell:
	docker-compose run --rm --no-deps $(CONTAINER) \
		python manage.py shell