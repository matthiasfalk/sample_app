FROM python:3.9.0-slim

WORKDIR app

RUN pip install flask gunicorn

COPY /sample_app ./sample_app
COPY wsgi.py /app

EXPOSE 8000

CMD gunicorn --bind 0.0.0.0:8000 "wsgi:create_app()"

