Docker microservice html2pdf
============================

Overview
--------

This docker image is based on the [wkhtmltopdf](https://wkhtmltopdf.org/) project and makes it simple to spawn a webapp that let generate pdf from a given url with just a http get query.

Docker image usage
------------------

run the container with the following

`docker run -e API_TOKEN=123 -e PORT=8030 --name my_container -dit -p 8030:8030 utopman/docker-microservice-html2pdf:latest`

Then you can generate a pdf with the following command

`wget -O /tmp/my.pdf "http://localhost:8030?token=123&url=http://perdu.com"`

Development
-----------

You have to install wkhtmltopdf locally to test the project. You may use commands provided in the Dockerfile to install it.

A docker compose file is provided to make it simpler to quickly build the container. Just add an environment variable as described below and run

`docker-compose up --build`

set token with environment variable

`echo API_TOKEN=123 >> .env`

Or run it locally by setup python flask app

`make install`

and run development server

`make dev`
