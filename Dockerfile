FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code

WORKDIR /code

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile Pipfile.lock /code/

RUN pipenv install --system

COPY . /code/

RUN chmod -R u+x /code/scripts
RUN ls -l /code/scripts