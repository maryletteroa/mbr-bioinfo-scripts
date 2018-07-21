# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:37:43

"""
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
