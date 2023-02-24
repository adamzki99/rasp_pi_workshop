#!/bin/sh
apt-get update && apt-get install -y \
    git \
    code \
    python3 \
    python3-dev \
    python3-pip \
    libgpiod2

apt full-upgrade
apt autoremove

pip3 install --upgrade --user pip \
    setuptools \
    wheel \
    gpiod \
    adafruit-circuitpython-lis3dh \
    adafruit-circuitpython-dht

echo "-----------------------------------------------"
echo "----------- Everything is set setup -----------"
echo "-----------------------------------------------"