FROM python:3.8.11

WORKDIR /var/task
COPY . .

# install project requirements
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip install pip --upgrade
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

# env variables
#ENV RUN_ENV 'prod'

CMD ["kedro", "run"]
