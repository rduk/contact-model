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

# Pull request steps

* Update your repository: 
    ```git pull origin master```
* Create a new branch to work on your ticket/task (branch name to have ticket number).
    ```git checkout -b TVCIS-1```
* Now we can work with this new branch.
* Add the files changed
    ```git add dag_1.py dag_2.py```
* Commit the changes to your local repository
    ```git commit -m "Introducing a new feature that will make everything work"```
* Push the local changes to the remote repository
    ```git push origin TTVIN-1```
* Now the branch is available in gitlab. In this step perform all necessary tests/sanity checks. If any issue with the data repeat step else create a new PR
* Create a Pull request in git lab:
    * Go to the project in gitlab
    * Go to Merge requests
    * Select your branch in the left and on the right the target branch (usually master)
    * Assign the reviewer and Create the Pull requests
    * Select your branch in the left and on the right the target branch (usually master)
    * Assign the reviewer and create the Pull Request(PR)
  
 
