# Quiz App #

## Install ##
    $ sudo apt install virtualenv
    $ sudo apt install python3.8-dev
    $ sudo apt install gcc
    $ virtualenv -p python3.8 env

    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ cd app

## Run tests ##
    $ python manage.py test quiz

## Run project ##
    $ python manage.py runserver

#### Visit the following URL to test application: ####
```
http://127.0.0.1:8000/quiz/
```
