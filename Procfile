web: gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
worker: celery -A config worker --loglevel=info
release: python manage.py migrate --noinput && python manage.py collectstatic --noinput --clear
