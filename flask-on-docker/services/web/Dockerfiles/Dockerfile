FROM osgeo/gdal:ubuntu-small-latest

WORKDIR /usr/src/app
RUN ls -la /

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update && apt-get install -y postgis              

RUN apt-get install -y python3-pip \
    && pip3 install --upgrade pip


COPY ./requirements.txt /usr/src/app/requirements.txt
RUN python3.6 -m pip install -r requirements.txt
