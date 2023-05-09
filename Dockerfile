FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN  apt-get update && apt-get install -y python3-pip && pip install -r requirements.txt  

COPY . .

CMD python server.py