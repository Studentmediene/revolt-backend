#!/usr/bin/env bash
# Migrate the Django database

$(dirname "$0")/run_django_command.sh migrate
