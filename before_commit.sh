set -eux
flake8 api_graphql app data_models
yapf -pir api_graphql app data_models -e '**/migrations' -e '**/snapshots'
isort -rc api_graphql app data_models
pytest
