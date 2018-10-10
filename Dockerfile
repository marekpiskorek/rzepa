FROM python:3.7

RUN pip install pipenv

RUN apt-get update -y && apt-get -y install postgresql-client

RUN groupadd -r rzepa --gid=999 && \
    useradd -r -g rzepa -d /rzepa/ --uid=999 -s /sbin/nologin -c "Docker image user" rzepa

COPY --chown=rzepa:rzepa . /rzepa/

RUN chmod +x /rzepa/scripts/*

USER rzepa

WORKDIR /rzepa/rzepa

RUN pipenv run pip install pip==18.0
RUN pipenv install --pre --dev
