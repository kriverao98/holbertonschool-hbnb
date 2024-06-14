#Dockerfile for hbnb project

FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /usr/holbertonschool-hbnb

RUN pip install uuid datetime pycountry

COPY requirements.txt / /usr/holbertonschool-hbnb/

RUN pip install --no-cache-dir -r requirements.txt

COPY API/ API/
COPY Model/ Model/
COPY Persistence/ Persistence/
COPY main.py .

EXPOSE 8000

ENV PORT 8000

VOLUME ["/usr/holbertonschool-hbnb/data"]

CMD ["gunicorn", '-b', "0.0.0.0:5000", "app:main"]
