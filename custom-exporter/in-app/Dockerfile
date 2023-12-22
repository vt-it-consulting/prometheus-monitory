FROM python:3.9-slim-buster

ADD requirements.txt requirements.txt
ADD in-app-flask-exporter.py in-app-flask-exporter.py
RUN apt update && apt-get install -y build-essential
RUN pip install uwsgi && pip install -r requirements.txt

ENTRYPOINT [ "uwsgi", "--http", "0.0.0.0:9999", "--wsgi-file", "in-app-flask-exporter.py", "--callable", "app", "--enable-threads"]
     