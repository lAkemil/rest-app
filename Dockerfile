FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
RUN apt-get install -y mongodb
RUN pip3 install pymongo

COPY app.py ./data/app.py

RUN pip3 install flask

EXPOSE 5000

CMD python3 /data/app.py
