#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# libraries
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# Instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use Pins 18,22,24,26 GPIO24,GPIO25,GPIO8,GPIO7
_step_pins = [24,25,8,7]
# Set all pins as output
for pin in _step_pins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)
# Define some settings
wait_time = 0.005
nb_steps_per_rev=2048

# Define simple sequence
step_count_1 = 4
seq1 = []
seq1 = [i for i in range(0, step_count_1)]
seq1[0] = [1,0,0,0]
seq1[1] = [0,1,0,0]
seq1[2] = [0,0,1,0]
seq1[3] = [0,0,0,1]
# Define advanced half-step sequence
step_count_2 = 8
seq2 = []
seq2 = [i for i in range(0, step_count_2)]
seq2[0] = [1,0,0,0]
seq2[1] = [1,1,0,0]
seq2[2] = [0,1,0,0]
seq2[3] = [0,1,1,0]
seq2[4] = [0,0,1,0]
seq2[5] = [0,0,1,1]
seq2[6] = [0,0,0,1]
seq2[7] = [1,0,0,1]
# Choose a sequence to use
seq = seq2
step_count = step_count_2

def steps(nb:int):
        step_counter = 0
        if nb<0: sign=-1
        else: sign=1
        nb=sign*nb*2 #times 2 because half-step
        for i in range(nb):
                for pin in range(4):
                        xpin = _step_pins[pin]
                        if seq[step_counter][pin]!=0:
                                GPIO.output(xpin, True)
                        else:
                                GPIO.output(xpin, False)
                step_counter += sign
        # If we reach the end of the sequence
        # start again
                if (step_counter==step_count):
                        step_counter = 0
                if (step_counter<0):
                        step_counter = step_count-1
                # Wait before moving on
                time.sleep(wait_time)

def motor_forward(revs):
    steps(int(revs*nb_steps_per_rev))
def motor_reverse(revs):
    steps(-1*int(revs*nb_steps_per_rev))