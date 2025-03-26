#FROM balenalib/raspberrypi5-ubuntu-python:20250202
FROM balenalib/raspberrypi4-64-debian-python:3.9-sid

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y --upgrade python3-setuptools

RUN apt-get update && apt-get install -y i2c-tools

# Clone and build LGPIO from source to get the _lgpio extension
#RUN git clone https://github.com/joan2937/python-lgpio.git /tmp/python-lgpio && \
 #   cd /tmp/python-lgpio && \
  #  make && \
   # make install && \
    #rm -rf /tmp/python-lgpio

RUN pip3 install requests lgpio rpi-lgpio redis 

COPY *.py ./
COPY *.ttf ./
COPY *.sh ./
COPY ./assets ./assets

CMD [ "bash", "start.sh" ]
