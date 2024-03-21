

docker-create:
	docker build -f extras/docker/development/Dockerfile --tag wger/server .

docker-push:
	docker tag wger/server diegofg93/wger-server
	docker push diegofg93/wger-server