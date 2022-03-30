# Raspberry Pi Workshop

## Improvements for next time
- [ ] A clear description of what shall be acomplished with the building and programming part. This description will be given out in paper form to each group. The description includes wiring diagrams, all the availabe functions from the __init__.py file aswell as a description.
- [x] Better function names
- [ ] New temp/humidity sensors


## Workshop Description
In this workshop we explore how easy it can be to collect data with a IoT-device. The workshop consist of three parts: Preperation, Action, Reaction.

### Preperation
The preperation of the workshop consist of a number of slides introducing the workshop takers into the concept of software and its importance in every day life.

Slides (Swedish): https://docs.google.com/presentation/d/1fgE1r-J_mvLzIIb5ylbsFcqQjccgmlm5yWpsgbVMwvg/edit?usp=sharing

### Action

Document to be handed out: *TBD*

The action part of the workshop is a hardware setup and coding activity there the workshop takers connect a light emitting diode (LED) and Temprature/Humidity sensor to the Raspberry Pi. Then the workshop takers are ment to figure out how they can get relevant information form the sensor to use it as a condition to turn on and off the LED.

We start by setting up the LED together, making everyone comfortable with setting up hardware. 

Then we go thru all the includes:

```py
from __init__ import * # we have built an abstraction layer so it is easier to use the intended hardware
from __motor_controll__ import * # if someone wants to use a motor
from time import sleep # used to make the LED blink
```

Then we must make a connectionbetween the hardware and software:

```py
createConnection()
```

Then we put everything in a infinit loop:

```py
while 1:
  # code goes here
```

### Reaction
When the action part is done it is time to think about what the workshop takers have acchived while coding.

## Wiring
![Alt text](wiring_schematic.png?raw=true "wiring_schematic.png")
Wiring schematic for connecting the AM2302(DHT22) and LED to the Raspberry Pi 

## OS
Download Link: https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-05-28/2021-05-07-raspios-buster-armhf.zip

Setup command, just paste in terminal and run. (NOTE: Program may fail to run if the hardware is not setup)

```batch
sudo apt install git && \\
sudo apt full-upgrade && \\
sudo apt install code && \\
sudo apt install python3 && \\
sudo apt install python3-pip && \\
sudo python3 -m pip install --upgrade pip setuptools wheel && \\
sudo pip3 install Adafruit_CircuitPython_DHT && \\
python3 -m pip install -U --user pip gpiod && \\
sudo apt install libgpiod2 && \\
sudo apt autoremove && \\
cd Documents/ && \\
git clone https://github.com/adamzki99/rasp_pi_workshop && \\ 
cd rasp_pi_workshop/ && \\
printf "\n\n\nEverything setup... Starting example.py\n\n\n" && \\
python3 example.py
```

## Code

### Input

- [x] AM2302       (Temperature + Humidity)

- [x] HC-SR501     (Motion Detection)

- [ ] MQ-2         (Gas)

- [ ] Pulsmesser   (Heart Rate Monitor)

- [ ] Sharp 2Y0A02 (Distance)

### Output

- [x] LED

- [x] Motor
