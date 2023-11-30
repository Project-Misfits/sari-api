#!/bin/sh
rm -rf /app/static/* && python manage.py collectstatic && gunicorn sariapi.wsgi:application --bind 0.0.0.0:8000 --workers 3
