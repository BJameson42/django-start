# Overview
Starting template for a Dockerized Django project. Includes minified files for Bootstrap 5 so they can be called locally in a development environment. You can switch these calls to a CDN (Content Delivery Network) later on if you so choose. 
<br><br>
## Containers
db = Postgres database<br>
db_backup = Scheduled backups for db container<br>
web = Django project served by gunicorn<br>
nginx = reverse proxy and static file server
<br><br>

## Prerequisites (run once per computer)
1. Install Python from Python.org
1. Install Docker Desktop
1. pip install docker-compose

## Prerequisites (run for every Django project)
1. Delete the hidden folder ".git"
1. Rename "django-start" folder to your project's name.
1. Change the 'name' value on line 2 of pyproject.toml to your project's name.
1. py generate_secretkey.py
1. poetry install
1. Rename ".env.sample" -> ".env"
    1. Copy/paste key generated in step #4 to 'SECRET_KEY' value.
    1. Replace value for 'DB_NAME' with your database name.
    1. Replace value for 'DB_USER' with your database username.
    1. Replace value for 'DB_PASSWORD' with your database user's password.


## Usage
1. Start Docker
    - docker-compose up -d --build
    - Navigate to "localhost" in your browser
1. Stop Docker
    - docker-compose down -v
1. View Docker logs
    - docker-compose logs -f
<br><br>

