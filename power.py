#!/usr/bin/env python
import Adafruit_BBIO.GPIO as GPIO
import time

HEADER = "P8"
PINS = (11, 12, 13, 14, 15, 16, 17, 18)

for pin in PINS:
	PORT = HEADER + "_" + str(pin)
	GPIO.setup(PORT, GPIO.OUT)
for _ in range(5):
	GPIO.output("P8_12", GPIO.LOW)
	time.sleep(2)
	GPIO.output("P8_12", GPIO.HIGH)
GPIO.cleanup()
