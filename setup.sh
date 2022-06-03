#!/bin/bash

if [ -d env ]; then
	echo "Virtual environment exists, delete it first."
	exit 1
fi

# Create a virtual environment:
python3 -m virtualenv env

# Activate virtual environment and install requirements:
source ./env/bin/activate
pip install -r requirements.txt

# Create a secret key:
SECRET_KEY="$(tr -dc 'A-Za-z0-9!#$%&()*+,-./:;<=>?@[\]^_`{|}~' </dev/urandom | head -c 30  ; echo)"
echo "SECRET_KEY = '$SECRET_KEY'" > CONotesWiki/.env
echo "DEBUG = 'False'" >> CONotesWiki/.env
echo "ALLOWED_HOSTS = '*'" >> CONotesWiki/.env
echo "GOOGLE_VERIFICATION = 'enter verification code here'" >> CONotesWiki/.env

# Migrate database:
python manage.py migrate

# Collect static files:
python manage.py collectstatic --no-input

deactivate

exit
