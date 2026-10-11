# syntax=docker/dockerfile:1

FROM python:alpine3.23

COPY app.py .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]