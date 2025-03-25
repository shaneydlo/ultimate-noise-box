#FROM balenalib/raspberrypi5-ubuntu-python:20250202
FROM balenalib/raspberrypi4-64-debian-python:3.7-sid

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    python3-dev \
    linux-headers-$(uname -r)

# Clone and build LGPIO from source to get the _lgpio extension
RUN git clone https://github.com/joan2937/python-lgpio.git /tmp/python-lgpio && \
    cd /tmp/python-lgpio && \
    make && \
    make install && \
    rm -rf /tmp/python-lgpio

# Upgrade pip and install gpiozero (which will use the LGPIO pin factory)
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install gpiozero

COPY *.py ./
COPY *.ttf ./
COPY *.sh ./
COPY ./assets ./assets

CMD [ "bash", "start.sh" ]
