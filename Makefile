
# Command to run migrations
migrate:
    python manage.py makemigrations
    python manage.py migrate

# Command to start the development server
runserver:
    python manage.py runserver

# Command to create a superuser
createsuperuser:
    python manage.py createsuperuser

# Command to run tests
test:
    python manage.py test

# Command to collect static files
collectstatic:
    python manage.py collectstatic --noinput
