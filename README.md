# Pokemon Crawler

Project started from https://docs.docker.com/compose/django/

## Project details
The project is built with Django and pokemon are rendered in templates and admin. 

## List of commands to run the project:
* `docker-compose up`
* `docker-compose exec web python -m pip install -r requirements.txt`
* `docker-compose exec web bash`
* `python manage.py migrate`
* `python manage.py createsuperuser` this is for admin
* `python manage.py test`

## Scaling
In this implementation the first time you open the pokemon list page, 
a call to pokeapi.co API is made and registers pokemon objects into the database, so this operation takes some seconds.
The other times that you open the page, the pokemon objects are taken from the database, so the page loading will be fast.

To be consistent with pokemon data (if they change from API) we have to make consistent API calls and insert or update existing objects. This will be always slow.
To make it faster, we can do a cron job (calling a Django management command) that calls the API and updates the database every ..... minutes, hours or days.

Or we can make it in a background task with Celery.