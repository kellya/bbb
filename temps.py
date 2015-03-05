#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
w1="/sys/devices/w1_bus_master1/28-000005e719c4/w1_slave"
w2="/sys/devices/w1_bus_master1/28-000005e5e1ec/w1_slave"

while True:
	raw1=open(w1,"r").read()
	raw2=open(w2,"r").read()
	print "Temp1: "+str(round(float(raw1.split("t=")[-1])/1000,2)) +"°C"
	print "Temp2: "+str(round(float(raw2.split("t=")[-1])/1000,2)) +"°C"
	print ""
	time.sleep(2)
