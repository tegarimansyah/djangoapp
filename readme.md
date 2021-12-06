
# Devips Application Monitoring Demo

  

[![N|Solid](https://www.alterra.id/wp-content/themes/alterra-wp/assets/revamp/img/logo_nav@2x.png)](https://alterra.id)

  
 
  
Repository ini merupakan demo aplikasi monitoring menggunakan custom metrics prometheus client



# Key Tech
* Django
* Prometheus Client
* Postgre

## Create and activate virtual env 
- pip install virtualenv
- virtualenv newenv
- source newenv/bin/activate

## Create postgre instance  
- cd backing-service
- docker-compose up -d


## Install requirement and setup env
- pip install -r requirements.txt
- export DATABASE_URL=postgresql://USERNAME:PASSWORD@localhost:5432/DB_NAME


## Run
- python manage.py runserver




## Available URL
- /random
- /delay
- /delay?delay=400 -> in miliseconds
- /setversion?version=0.1.2 -> version in string
- /health
- /metrics


  

