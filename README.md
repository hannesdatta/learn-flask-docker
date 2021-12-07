# Learning app development with Flask and Docker

In this repository, I started to learn how to deploy Flask apps using Docker containers (which I need for ["Pulse" (open education tracking & performance app)](https://github.com/hannesdatta/pulse) and ["Research Cloud" (research cloud for co-authors on EC2)](https://github.com/hannesdatta/private-research-cloud).

## Features
- displaying "Hello world"
- using environment variables (e.g., for non-sensitive information)
- reading in secret credentials from a `.txt` file

## Running instructions

### Deployment in development mode

- `export FLASK_APP=app`
- `flask run`

### Deployment in local container
1. Install prerequisites (Docker, AWS, Lightsail) from [here](https://aws.amazon.com/getting-started/hands-on/serve-a-flask-app/)

2. Build docker image: `docker-compose build`

3. Run docker image: `docker-compose up`

### Deployment on AWS Lightsail

tbd

## Misc.

### Useful commands

- View running docker images: `docker ps`

- Remove docker images: `docker rm <IMAGE_NAME-SEE-DOCKER-PS`>

- Start/stop docker images: `docker start <IMAGE>`, `docker stop <IMAGE>`

## Acknowledgement

This repository has been inspired by, among others:

- https://aws.amazon.com/getting-started/hands-on/serve-a-flask-app/
- https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04
