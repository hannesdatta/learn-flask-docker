# Learning app development with Flask and Docker

In this repository, I started to learn how to deploy Flask apps using Docker containers.

## Features
- displaying "Hello world"
- using environment variables (e.g., for non-sensitive information)
- reading in secret credentials from a `.txt` file

## Running instructions

1. Install prerequisites (Docker, AWS, Lightsail) from [here](https://aws.amazon.com/getting-started/hands-on/serve-a-flask-app/)

2. Build docker image: `docker-compose build`

3. Run docker image: `docker-compose up`

## Inspired by...
- https://aws.amazon.com/getting-started/hands-on/serve-a-flask-app/
- https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04
