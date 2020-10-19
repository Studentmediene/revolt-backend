#!/usr/bin/env bash
# Run a Django command in the Docker container
# This file is the basis for all the other scripts

# Run as the current user, so that any files created are not owned by root
docker-compose run \
  --rm \
  --user $(id -u):$(id -g) \
  backend \
  python manage.py "$@"
