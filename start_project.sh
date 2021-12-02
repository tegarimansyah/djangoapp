#!/usr/bin/bash

PROJECT_NAME=$1

django-admin startproject config .

# Create settings skeleton
mkdir -p config/settings/{components,env}
touch config/settings/__init__.py
touch config/settings/env/{__init__,base,staging,prod}.py
touch config/settings/components/{__init__,database,common,email,logging,storage}.py

# Add other project directories
mkdir -p $PROJECT_NAME/{static,templates,media}

# Add basic settings
mv config/settings.py config/settings/env/local.py

cat << EOF > config/settings/__init__.py
from split_settings.tools import optional, include

include(
    'components/database.py',
    'env/base.py',
)
EOF

# Install and setup basic settings
pipenv install \
    # settings 
    django-split-settings django-environ
    # database
    psycopg2

python manage.py migrate
python manage.py createsuperuser

