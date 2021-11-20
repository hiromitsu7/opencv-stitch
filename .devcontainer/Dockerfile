FROM ubuntu:20.04

# tzdataのプロンプトを出さないようにする
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-dev python3-pip python3-setuptools libopencv-dev && \
    apt-get install -y iputils-ping vim less man jq bc zip git curl wget bash-completion lsof tree htop traceroute  dnsutils iproute2 git && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m pip install --no-cache-dir --upgrade pip setuptools && \
    python3 -m pip install --no-cache-dir scikit-build && \
    python3 -m pip install --no-cache-dir numpy && \
    python3 -m pip install --no-cache-dir opencv-python && \
    adduser --disabled-password --gecos "Developer" devuser && \
    adduser devuser sudo && \
    echo "devuser ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    # generate .sudo_as_admin_successful to prevent sodu from showing guide message
    touch ~devuser/.sudo_as_admin_successful && \
    # allow devuser to install files to /usr/local without sudo prefix
    chown -R root:sudo /usr/local && \
    mkdir /home/devuser/work

USER devuser

WORKDIR /home/devuser

ENV LANG=C.UTF-8
