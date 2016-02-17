#!/usr/bin/env python

from daemonize import Daemonize
import thread
import os
import sys
from datetime import datetime
from time import sleep

pidfile = "/tmp/hydra.pid"

sys.path.append("/root/bbb/hydra")
os.environ["DJANGO_SETTINGS_MODULE"] = "hydra.settings"

from temp.models import Temp


def writetemp():
	value = Temp(timestamp=datetime.strptime("20150101000000", '%Y%m%d%H%M%S'),
			reading=76.8)
	value.save()
	sleep(30)

def main():
	thread.start_new_thread(writetemp)

daemon = Daemonize(app="hydra",pid=pidfile, action=main)
daemon.start()
