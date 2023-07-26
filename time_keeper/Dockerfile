FROM python:3.11.4-alpine3.18 

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver" ]

# ENTRYPOINT [ "python", "main.py" ]

# CMD [ "python", "manage.py", "runserver" ]
