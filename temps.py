#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import glob

devroot = "/sys/devices/w1_bus_master1"


def ctof(rawval):
	return str(((rawval*9)/5)+32)
	
tempint = []
for tempdev in glob.glob(devroot+'/28-*/w1_slave'):
	tempint.append(tempdev)

while tempint > 0:
	for device in tempint:
		raw = open(device,"r").read()
		print "Temp"+str(tempint.index(device))+": "+str(round(float(raw.split("t=")[-1])/1000,2)) +"°C"
	print ""
	time.sleep(2)
