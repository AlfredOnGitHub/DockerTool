#imagen base
FROM python:latest
#archivos locales a imagen
COPY ./tool /tool
#workird
WORKDIR /tool
#escuchar puertos
EXPOSE 8000
#django y pillow
RUN pip install \
    django\
    pillow
#comando
CMD ["python","./manage.py","runserver"]

