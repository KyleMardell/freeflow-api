release: python manage.py makemigrations && python manage.py migrate
web: gunicorn freeflow_api.wsgi