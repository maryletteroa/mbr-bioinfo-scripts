# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:37:31

'''
Filters concordant sam files
Requires samtools
'''


from sys import argv, exit
from os import system

help = """
Usage: foo.py <sequence.sam>
"""

try: argv[1]
except IndexError:
        print help
        exit()

samtools_path="~/apps/samtools-1.3.1/samtools"

conc_exec = """{0} view -hS {1} | awk 'substr($0,1,1) == "@" || ($2==83 || $2==99 || $2==147 || $2==163) && ($9 != 0) {{print;}}'""".format(samtools_path, argv[1])

system(conc_exec)
# print(conc_exec)
