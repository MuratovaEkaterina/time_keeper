python manage.py migrate --noinput

# if [ "$SUPERUSER_USERNAME" ]
# then
#     # python manage.py createsuperuser \
DJANGO_SUPERUSER_USERNAME="$SUPERUSER_USERNAME" \
DJANGO_SUPERUSER_PASSWORD="$SUPERUSER_PASSWORD" \
DJANGO_SUPERUSER_EMAIL="$SUPERUSER_EMAIL" \
python manage.py createsuperuser --noinput

# python manage.py createsuperuser \
#     --noinput \
#     --username $SUPERUSER_USERNAME \
#     --email $SUPERUSER_EMAIL \
#     --password $SUPERUSER_PASSWORD \
# fi

# $@ 

# docker exec -it time_keeper python manage.py createsuperuser


python manage.py runserver --noreload 0.0.0.0:8000 