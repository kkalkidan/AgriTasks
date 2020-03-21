FROM osgeo-gdal-flask:1.0 
RUN locale -a
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN echo $LC_ALL
RUN echo $LANG
RUN locale -a
# RUN python3.6 -c 'print(u"\u2122");'
COPY .  .
RUN python3.6 -m pip install pytest
RUN ls -a .
RUN ls test/
# CMD ["pytest", "test_api.py"]
# CMD [python3.6, "/Users/kalkidanfekadu/tutorial/FromScratch/flask-on-docker/services/web/test/test_api.py"]
