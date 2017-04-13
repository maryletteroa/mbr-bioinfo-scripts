#!/usr/bin/env python

from sys import argv, exit
from os import system

help = """
Usage: ./filt_concordant.py <sequence.sam>
"""

try: argv[1]
except IndexError:
        print help
        exit()

samtools_path="~/apps/samtools-1.3.1/samtools"

conc_exec = """{0} view -hS {1} | awk 'substr($0,1,1) == "@" || ($2==83 || $2==99 || $2==147 || $2==163) && ($9 != 0) {{print;}}'""".format(samtools_path, argv[1])

system(conc_exec)
# print(conc_exec)
