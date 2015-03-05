#!/usr/bin/env python
import Adafruit_BBIO.PWM as PWM
import time

PWM.start("P8_13", 0)
for i in range(0, 100):
	PWM.set_duty_cycle("P8_13", float(i))
	time.sleep(.05)
for i in range(100, 0, -1):
	PWM.set_duty_cycle("P8_13", float(i))
	time.sleep(.05)

PWM.stop("P8_13")
PWM.cleanup()
