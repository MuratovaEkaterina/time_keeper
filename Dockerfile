FROM python:3.11.4-alpine3.18 

ENV SUPERUSER_USERNAME=admin
ENV SUPERUSER_EMAIL=example@example.com
ENV SUPERUSER_PASSWORD=passwordqwerty12

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt
# 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# 
# ENV PYTHONUNBUFFERED=1

CMD [ "sh", "run.sh" ] 

