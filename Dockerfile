FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /django
WORKDIR /django

ADD requirements.txt /django/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

ADD . /django/

