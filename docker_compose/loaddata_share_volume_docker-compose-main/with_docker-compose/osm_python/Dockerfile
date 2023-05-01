
FROM python:3.8-slim-buster
WORKDIR /app
#RUN mkdir /app
COPY requirements.txt /app
#WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080

#CMD ["tail", "-f", "/dev/null"] #for testing the container filesytem
CMD ["python3", "osm.py"]


