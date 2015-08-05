# consul-template-docker-compose

basic project to show how to scale up and down _docker-compose_ services using consul-template and nginx

## Requirements

[Docker Compose](https://docs.docker.com/compose/) 1.3 or later

## Getting started

Run the following command in terminal:

    docker-compose up

open your browser to `http://localhost:8500/ui/`. There you will find a _webapp_ service, running on a single node (i.e. a single Docker container)

    docker-compose scale webapp=5

check again `http://localhost:8500/ui` to ensure that there are now five _webapp_ instance.

Make a few requests to `http://localhost:8080/` and then run `docker-compose logs` to see how requests are processed by different _webapp_ instances.

You can now scale down the _webapp_ service without having any down time, e.g.:

    docker-compose scale webapp=2

Again, you can check `http://localhost:8500/ui` to see that there are now only two instances.