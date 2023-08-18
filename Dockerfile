FROM python:3.11-slim

# Get TG bot token from build agrs and put it into env
ARG BOT_TOKEN
ENV BOT_TOKEN=$BOT_TOKEN

# prevents Python from copying pyc files to the container
ENV PYTHONDONTWRITEBYTECODE 1
# ensures that Python output is logged to the terminal,
# making it possible to monitor Django logs in realtime
ENV PYTHONUNBUFFERED 1

# being used at container running stage
# ENV ENVIRONMENT=$ENV_ARG

# Initialize the environment
WORKDIR /usr/src/app
ADD ./pyproject.toml .
ADD ./poetry.lock .
# RUN pip install pip==21.3.1
RUN pip install -U pip poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Web server and reverse proxy configuration
# RUN rm -rf /usr/share/nginx/html/*
# COPY --from=node_build /home/dist /usr/share/nginx/html
# ADD ./deploy_confs/nginx.conf /etc/nginx/nginx.conf
# ADD ./deploy_confs/launch.sh /usr/bin
# ADD ./deploy_confs/launch_local.sh /usr/bin
# RUN chmod +x /usr/bin/launch*.sh

# Copy application files
ADD . .

# EXPOSE 80

CMD ["python", "main.py"]