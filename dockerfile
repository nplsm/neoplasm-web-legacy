FROM python:3.7

RUN adduser --system --group neoplasm

ENV APP_HOME=/home/neoplasm/neoplasm-web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME
RUN chown -R neoplasm:neoplasm $APP_HOME

RUN pip install pipenv && pipenv install --system

USER neoplasm

