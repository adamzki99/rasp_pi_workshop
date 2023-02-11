# Raspberry Pi Workshop

## Until next time
### From 7 April 2022
- [ ] Two seperate scripts, one for "apt install"-stuff and one for "pip3 install"-stuff
- [ ] Update and fix all errors in the wiring schematic
- [ ] The current library for the temp/humidity sensor do not work, this needs to be chaged and tested that it works with the Raspberry Pi 4
- [ ] Better instructions: Add that there is a wiring schematic for the LED and sensor, as well as instructions on how to run the python code
### From 8 December 2022
- [ ] New temp/humidity sensors with a integrated resistor: https://www.amazon.se/AZDelivery-Temperatursensor-Fuktgivare-Kretskort-kompatibel/dp/B078SVZB1X/ref=sr_1_7?crid=2DRKBQSXON1U6&keywords=DHT22&qid=1649316053&sprefix=dht22%2Caps%2C87&sr=8-7


## Workshop Description
In this workshop we explore how easy it can be to collect data with a IoT-device. The workshop consist of three parts: Preparation, Action, Reaction.

### Preparation
The preparation of the workshop consist of a number of slides introducing the workshop takers into the concept of software and its importance in every day life.

Slides (Swedish): https://docs.google.com/presentation/d/1fgE1r-J_mvLzIIb5ylbsFcqQjccgmlm5yWpsgbVMwvg/edit?usp=sharing

### Action

Document to be handed out: https://github.com/adamzki99/rasp_pi_workshop/blob/main/instructions/instructions_v1.md

The action part of the workshop is a hardware setup and coding activity there the workshop takers connect a light emitting diode (LED) and Temperature/Humidity sensor to the Raspberry Pi. Then the workshop takers are meant to figure out how they can get relevant information form the sensor to use it as a condition to turn on and off the LED.

We start by setting up the LED together, making everyone comfortable with setting up hardware.

### Reaction
When the action part is done it is time to think about what the workshop takers have achieved while coding.

## Wiring
![wiring schematic](images/wiring_schematic.png)

Wiring schematic for connecting the AM2302(DHT22) and LED to the Raspberry Pi

## OS
Download Link: https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-05-28/2021-05-07-raspios-buster-armhf.zip

Setup command, just paste in terminal and run.

```shell
sudo install_workshop_dependencies.sh
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
