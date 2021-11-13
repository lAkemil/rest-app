FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "./app.py"]