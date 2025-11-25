release: python manage.py migrate --noinput && python manage.py collectstatic --noinput
web: gunicorn kazigoproject.wsgi:application --log-file -