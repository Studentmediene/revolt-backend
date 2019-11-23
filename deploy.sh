#!/bin/bash
GIT_BRANCH=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')


# Use sudo to prompt for sudo password before deploying
echo "Please enter the password for the current user:"
sudo echo "Deploying kapina-backend on branch $GIT_BRANCH..."
git pull

source venv/bin/activate
export $(grep -v '^#' .env | xargs)

pip install -r requirements.txt
./manage.py migrate
./manage.py collectstatic --no-input
sudo systemctl restart kapina-backend.service
echo "Successfully deployed kapina-backend on branch $GIT_BRANCH."