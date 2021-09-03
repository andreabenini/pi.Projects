#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Interactive utility for testing PWM and fan duty cycle
#
# pylint: disable=import-error

import sys
import time
try:
    import RPi.GPIO as GPIO
except Exception as E:
    print("\nRPi module not found, aborting program")
    print(str(E))
    print("Please install python-raspberry-gpio package\n")
    sys.exit(1)

FAN_PIN  = 18                   # GPIO 18, PWM, pin 12
PWM_FREQ = 25                   # PWM frequency

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)

fan = GPIO.PWM(FAN_PIN, PWM_FREQ)
fan.start(0)
try:
    print("Enter Duty Cycle (0..100)")
    while 1:
        fanSpeed = float( input("Fan Speed: ") )
        fan.ChangeDutyCycle(fanSpeed)
except(KeyboardInterrupt):
    print("\n\nCtrl+C. Interrupted by keyboard")
    GPIO.cleanup()
    sys.exit()
