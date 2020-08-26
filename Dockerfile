FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /Code
WORKDIR /Code

COPY requirements.txt /Code
RUN python -m pip install -r requirements.txt

COPY . /Code