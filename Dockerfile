FROM python:3.9-alpine3.15

COPY . ./data/

RUN pip3 install -r /data/requirements.txt

EXPOSE 5000
CMD python3 /data/app.py
