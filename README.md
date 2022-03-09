# CONTENT INGEST SERVICE

Main goals of this project:
* Process and Analyse **VOD** metadata/content
* Process **Linear** Metadata

# Setup and Execute

Steps to follow to set this project up in your local machine.

Clone the repository:
```
you@machine:~$ mkdir -p ~/workspace && cd ~/workspace
you@machine:~/workspace$ git clone ssh://git@gitlab.dtoneapp.telekom.net:filipe.lino/airflow-dags.git
```
Install and setup the airflow project
```
* docker-compose down -d 
* ./build_docker_image.sh
* docker-compose run airflow-worker db upgrade
* docker-compose up -d 
```

_Note: If these is any permission related issue while running docker-compose command in docker-compose.yaml please change this line user: "${AIRFLOW_UID:-50000}:${AIRFLOW_GID:-50000}" with user: "${AIRFLOW_UID:-0}:${AIRFLOW_GID:-0}"_
