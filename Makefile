IMAGE   = python-opencv

build:
	docker build -t $(IMAGE) .

run:
	docker run --rm -v $$PWD/work:/home/devuser/work -it $(IMAGE) bash

rmi:
	docker rmi $(IMAGE)