#!/bin/sh
flake8 api_graphql app data_models
yapf -pdr api_graphql app data_models -e '**/migrations' -e '**/snapshots'
isort -c -rc api_graphql app data_models
py.test --cov-report=xml
