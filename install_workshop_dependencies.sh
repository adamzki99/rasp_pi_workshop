#!/bin/sh
sudo apt install git
sudo apt full-upgrade
sudo apt install code
sudo apt install python3
sudo apt-get install python3-dev python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install --install-option="--force-pi" Adafruit_DHT
sudo pip3 install Adafruit_Python_DHT
python3 -m pip install -U --user pip gpiod
sudo apt install libgpiod2
sudo apt autoremove
echo "-----------------------------------------------"
echo "----------- Everything is set setup -----------"
echo "-----------------------------------------------"