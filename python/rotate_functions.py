import RPi.GPIO as GPIO
import time
from DRV8825 import DRV8825
import math 


def rotate(motor,rotations,speed): #default speed = 0.001
    msteps = math.ceil(abs(rotations) * 800)
    direction = 'backward'
    if(rotations<0): #counterclockwise negative(towards motor), clockwise positive(away from motor)
        direction = 'forward'

    if(speed > 5):
        speed = 5
    mspeed = 0.001 / speed
    motor.TurnStep(Dir=direction, steps=msteps, stepdelay = mspeed)