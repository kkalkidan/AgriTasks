FROM osgeo-gdal-flask:1.0 
RUN locale -a
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN echo $LC_ALL
RUN echo $LANG
RUN locale -a
# RUN python3.6 -c 'print(u"\u2122");'
COPY . /usr/src/app/
# RUN python3.6 -m  pip install pytest
RUN ls -a
# ENV FLASK_APP=project/__init__.py
# ENV FLASK_ENV=development
# ENV DATABASE_URL=postgresql://test:test@db:5432/test
# ENV SQL_HOST=db
# ENV SQL_PORT=5432
# ENV DATABASE=postgres
# CMD ["python3.6", "manage.py run -h 0.0.0.0"]
