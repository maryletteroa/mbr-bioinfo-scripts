#!/usr/bin/env python
"""
@MaryletteRoa

Usage: cat *timer | ./sumtime.py

Prints realtime in seconds.
"""

import fileinput
from sys import exit
import time

tsec = 0
for line in fileinput.input():
        realtime=line.split(" real")[0]
        if realtime.count(":") == 1:
                min=float(realtime.split(":")[0])*60
                sec=float(realtime.split(":")[1])
                t = min+sec
        elif realtime.count(":") == 2:
                hour=float(realtime.split(":")[0])*60*60
                min=float(realtime.split(":")[1])*60
                sec=float(realtime.split(":")[2])
                t = hour+min+sec
        tsec = tsec + t
#ttime = time.strftime("%M:%S", time.gmtime(tsec))
#print ttime
print( tsec)
