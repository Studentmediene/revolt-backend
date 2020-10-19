#!/usr/bin/env bash
# Create Django migration files

$(dirname "$0")/run_django_command.sh makemigrations
