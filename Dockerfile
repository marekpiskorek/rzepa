FROM python:3.7

RUN pip install pipenv

RUN apt-get update -y && apt-get -y install postgresql-client nginx supervisor

RUN groupadd -r rzepa --gid=999 && \
    useradd -r -g rzepa -d /rzepa/ --uid=999 -s /sbin/nologin -c "Docker image user" rzepa

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

COPY --chown=rzepa:rzepa . /rzepa/

RUN chmod +x /rzepa/scripts/*

USER rzepa

WORKDIR /rzepa/rzepa

# There is a bug with latest pipenv and pip 18.1, therefore we need to ensure version of pip that works well with pipenv.
RUN pipenv run pip install pip==18.0

RUN pipenv install --pre --dev

EXPOSE 80
CMD ["supervisord", "-n"]
