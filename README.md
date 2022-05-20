# Overview
Starting template for a Dockerized Django project.
<br><br>
## Containers
db = Postgres database<br>
db_backup = Scheduled backups for db container<br>
web = Django project served by gunicorn<br>
nginx = reverse proxy and static file server
<br><br>
## Usage

### Start Docker
docker-compose up -d --build<br>
<br>
### Stop Docker
docker-compose down -v<br>
<br>
### View Docker logs
docker-compose logs -f<br>
<br>

