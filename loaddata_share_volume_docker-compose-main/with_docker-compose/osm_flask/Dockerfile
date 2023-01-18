FROM python:3.8-slim-buster

#RUN mkdir /app
WORKDIR /app
RUN ls
COPY requirements.txt /app
#WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
RUN ls
#CMD ["tail", "-f", "/dev/null"] #for testing the container filesystem
CMD ["python3", "osm_app.py"]
