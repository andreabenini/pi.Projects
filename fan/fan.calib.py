#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Interactive utility for testing PWM and fan duty cycle
#
import sys
import time
import RPi.GPIO as GPIO

FAN_PIN  = 18                   # GPIO 18, PWM, pin 12
PWM_FREQ = 25                   # PWM frequency

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)

fan = GPIO.PWM(FAN_PIN, PWM_FREQ)
fan.start(0);
try:
    print("Enter Duty Cycle (0..100)")
    while 1:
        fanSpeed = float( input("Fan Speed: ") )
        fan.ChangeDutyCycle(fanSpeed)
except(KeyboardInterrupt):
    print("Fan ctrl interrupted by keyboard")
    GPIO.cleanup()
    sys.exit()
