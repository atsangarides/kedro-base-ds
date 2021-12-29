# syntax=docker/dockerfile:experimental
FROM python:3.8.11
# add ssh known hosts
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

# install project requirements
COPY src/requirements.txt /tmp/requirements.txt
COPY src/private-requirements.txt /tmp/private-requirements.txt
RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt
RUN --mount=type=ssh pip install -r /tmp/private-requirements.txt && rm -f /tmp/private-requirements.txt

# env variables
#ENV RUN_ENV 'prod'

# add kedro user
ARG KEDRO_UID=999
ARG KEDRO_GID=0
RUN groupadd -f -g ${KEDRO_GID} kedro_group && \
useradd -d /home/kedro -s /bin/bash -g ${KEDRO_GID} -u ${KEDRO_UID} kedro

# copy the whole project except what is in .dockerignore
WORKDIR /home/kedro
COPY . .
RUN chown -R kedro:${KEDRO_GID} /home/kedro
USER kedro
EXPOSE 8888
CMD ["kedro", "run"]