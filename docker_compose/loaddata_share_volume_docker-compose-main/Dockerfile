
FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
RUN chmod +x script.sh
CMD [ "/app/script.sh"]




