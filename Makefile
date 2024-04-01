.PHONY: clean up down

default: up

clean:
	@echo "*** Cleaning repo of unnecessary artifacts... ***"
	rm -rf excel

up: clean
	@echo "*** Building and running the python excel builder with local db... ***"
	docker-compose -f docker-compose.yaml up -d --build --remove-orphans

down:
	@echo "*** Stopping the python excel builder with local db... ***"
	docker-compose -f docker-compose.yaml down --remove-orphans
	make clean
