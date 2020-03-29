#imagen base
FROM python:latest
#archivos locales a imagen
COPY ./tool /tool
#workird
WORKDIR /tool
#escuchar puertos
EXPOSE 5000
#django y pillow
RUN pip install \
    django\
    pillow
#comando
CMD ["python","./manage.py","runserver","0.0.0.0:5000"]

