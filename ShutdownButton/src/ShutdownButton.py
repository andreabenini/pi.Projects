#!/usr/bin/env python
#----------------------------------------------------------------------------------------
# Name:        ShutdownButton.py
#
# Purpose:     Script for safely shutting down the Pi with a physical shutdown button
#              connnected on GPIO output. Script run as a service.
#              Connected circuit allows to safely shutdown the Pi or forces a reboot
#              (with a 2s long press) when the system is freezed
# See:         Script based on "paulv" work (2016-03-20) from RPi forums with its circuit
#
# Author:      Andrea (Ben) Benini
#
# Created:     2017/05/20
# Copyright:   CC0
# Licence:     CC0       [https://creativecommons.org/share-your-work/public-domain/cc0/]
#----------------------------------------------------------------------------------------
import RPi.GPIO as GPIO
import subprocess


### Setup
DEBUG = False
GPIO.setmode(GPIO.BCM) # use GPIO numbering
GPIO.setwarnings(False)
BUTTON = 4                                               # GPIO-4
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # pulled-up when circuit is not connected


### Main
def main():
    print "Program started"
    while True:
        # set an interrupt on a falling edge and wait for it to happen
        GPIO.wait_for_edge(BUTTON, GPIO.FALLING)
        if DEBUG:
            print "Button detected ", GPIO.input(BUTTON)
        else:
            print "Shutdown requested, Halting the RPi now ! "
            subprocess.call(['halt'], shell=True, \
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == '__main__':
    main()
