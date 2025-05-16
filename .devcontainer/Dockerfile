ARG VARIANT=3
FROM --platform=linux/amd64 mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

COPY .devcontainer/requirements.txt /tmp/pip-tmp/
COPY .devcontainer/requirements.yml /tmp/ansible-tmp/

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y software-properties-common

# Install Dependencies
RUN apt -y install \
    ca-certificates \
    curl \
    gnupg \
    libonig-dev \
    libssh-dev \
    sshpass

RUN apt update

# Install Python Packages
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

# Install Containerlab
RUN echo "deb [trusted=yes] https://netdevops.fury.site/apt/ /" | \
    tee -a /etc/apt/sources.list.d/netdevops.list

RUN apt update && apt install containerlab

RUN usermod -aG clab_admins vscode

# Install tmux
RUN apt install -y tmux

# Install kubectl
RUN apt install -y apt-transport-https ca-certificates curl gnupg

RUN curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.32/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
# allow unprivileged APT programs to read this keyring
RUN chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg

# This overwrites any existing configuration in /etc/apt/sources.list.d/kubernetes.list
RUN echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.32/deb/ /' | tee /etc/apt/sources.list.d/kubernetes.list
# helps tools such as command-not-found to work correctly
RUN chmod 644 /etc/apt/sources.list.d/kubernetes.list

RUN apt update
RUN apt install -y kubectl kubectx
RUN apt install -y git-lfs

# Install Ansible Dependencies
USER vscode
RUN ansible-galaxy collection install -r /tmp/ansible-tmp/requirements.yml

USER root
RUN rm -rf /tmp/ansible-tmp
