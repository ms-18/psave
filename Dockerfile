FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code

WORKDIR /code

COPY ./Pipfile /code/

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt

COPY . /code/