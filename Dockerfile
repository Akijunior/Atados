FROM python:3

LABEL maintainer="luijunior96@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir /webapps

WORKDIR /webapps

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get clean && apt-get upgrade -y && apt-get install -y locales
RUN locale-gen pt_BR.UTF-8

RUN sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen

ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt
ENV LC_ALL pt_BR.UTF-8

RUN pip install -U pip setuptools
COPY requirements.txt /webapps/
RUN pip install -r /webapps/requirements.txt
ADD . /webapps/

EXPOSE 5440