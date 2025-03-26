FROM balenalib/raspberrypi4-64-debian-python:3.9-sid

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y --upgrade python3-setuptools

RUN apt-get update && apt-get install -y i2c-tools

RUN pip3 install requests lgpio rpi-lgpio redis 

COPY *.py ./
COPY *.ttf ./
COPY *.sh ./
COPY ./assets ./assets

CMD [ "bash", "start.sh" ]
