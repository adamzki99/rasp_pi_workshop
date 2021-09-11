from time import sleep
from __init__ import *
from __motor_controll__ import *

createConnection()

while 1:
    motorForward(0.25)
    sleep(1)
    motorReverse(0.25)
    sleep(1)