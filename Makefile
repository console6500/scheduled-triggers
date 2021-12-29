build:
	docker build --tag=super-amazing-web-app .

up: down
	docker compose up

detach: down
	docker compose up --detach
	sleep 1

test:
	curl --silent http://localhost:9000 | grep hello

down:
	@docker compose down --rmi local
