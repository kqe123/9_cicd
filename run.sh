#!/bin/sh

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn config.wsgi:application --bind 0.0.0.0:8000 &
unlink /etc/nginx/sites-enabled/default
nginx -g 'daemon off;'