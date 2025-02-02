# Sari API
Django powered API

## Development
### Requrements
- Docker
- Git
- DBMS (dbeaver,.. etc)

### Bulding the image
```bash
docker compose build web
```
### Starting server
```bash
docker compose up web
```
### Creating super user
```bash
docker compose run --rm web python manage.py createsuperuser
```
### Migrations
Generate migration files
```bash
docker compose run --rm web python manage.py makemigrations
```
Run migration
```bash
docker compose run --rm web python manage.py migrate
```
