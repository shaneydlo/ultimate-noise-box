#FROM balenalib/raspberrypi5-ubuntu-python:20250202
FROM balenalib/raspberrypi4-64-ubuntu-python:3.8

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \ 
    git \
    python3-lgpio \
    build-essential

# Clone and build LGPIO from source
RUN git clone https://github.com/joan2937/lg.git /tmp/python-lgpio && \
    cd /tmp/python-lgpio && \
    make && \
    make install && \
    rm -rf /tmp/python-lgpio

#    apt-get update && apt-get install -y python3-pip python3-lgpio python3-libgpiod

COPY requirements.txt requirements.txt

# RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install gpiozero

# *** tested versions of installed libraries ***
# numpy 1.21.5
# pillow 9.1.0
# RPi.GPIO 0.7.1
# adafruit-circuitpython-rgb-display 3.10.12
# requests 2.27.1
# redis 4.2.2
# adafruit-circuitpython-seesaw 1.10.8

COPY *.py ./
COPY *.ttf ./
COPY *.sh ./
COPY ./assets ./assets

CMD [ "bash", "start.sh" ]
