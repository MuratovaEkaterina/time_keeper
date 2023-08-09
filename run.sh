python manage.py migrate --noinput

# if [ "$SUPERUSER_USERNAME" ]
# then
#     # python manage.py createsuperuser \
docker exec -it time_keeper python manage.py createsuperuser \
    --noinput \
    --username $SUPERUSER_USERNAME \
    --email $SUPERUSER_EMAIL \
    --password $SUPERUSER_PASSWORD \
# fi

# $@ 

# docker exec -it time_keeper python manage.py createsuperuser



python manage.py runserver --noreload 0.0.0.0:8000 