# Jenkins Dockerfile
FROM jenkins/jenkins:lts

USER root

# Install Python, Docker CLI, and Git
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv docker.io git && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*

# Install docker-compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Add Jenkins user to Docker group (without creating it)
RUN usermod -aG docker jenkins


# Configure Git
ARG GIT_USER_NAME
ARG GIT_USER_EMAIL

RUN git config --global user.name "${GIT_USER_NAME}" && \
    git config --global user.email "${GIT_USER_EMAIL}"

USER jenkins
