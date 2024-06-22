#Dockerfile for hbnb project

FROM python:3.8

WORKDIR /usr/holbertonschool-hbnb

COPY . /usr/holbertonschool-hbnb/

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8000

EXPOSE 8000

VOLUME ["/usr/holbertonschool-hbnb/Persistence"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
