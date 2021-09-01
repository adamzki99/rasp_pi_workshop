# Raspberry Pi Workshop


## Wiring
![Alt text](photos/wiring_schematic.png?raw=true "wiring_schematic.png")

Wiring schematic for connecting the AM2302 and LED to the Raspberry Pi 

## OS
Download Link: https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-05-28/2021-05-07-raspios-buster-armhf.zip

Setup command (Just paste in terminal and run. Program may fail to run if the hardware is not setup)
``
cd && sudo apt install git && sudo apt install python3 && sudo apt install python3-pip && sudo python3 -m pip install --upgrade pip setuptools wheel && sudo pip3 install Adafruit_CircuitPython_DHT && python3 -m pip install -U --user pip gpiod && sudo apt install libgpiod2 && sudo apt autoremove && cd Documents/ && git clone https://github.com/adamzki99/rasp_pi_workshop ; cd rasp_pi_workshop/ && printf "\n\n\nEverything setup... Starting example.py\n\n\n" &&python3 example.py
``

