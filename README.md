# Overview
Starting template for a Dockerized Django project. Includes minified files for Bootstrap 5 so they can be called locally in a development environment. You can switch these calls to a CDN (Content Delivery Network) later on if you so choose. 
<br><br>
## Containers
db = Postgres database<br>
db_backup = Scheduled backups for db container<br>
web = Django project served by gunicorn<br>
nginx = reverse proxy and static file server
<br><br>
## Usage
1. Rename ".env.sample" -> ".env"
2. In .env file, update:
    - DB_NAME
    - DB_PASSWORD
    - DB_USER
3. Start Docker
    - docker-compose up -d --build
    - Navigate to "localhost" in your browser
4. Stop Docker
    - docker-compose down -v

<br><br>
#### View Docker logs<br>
docker-compose logs -f<br>
<br>

