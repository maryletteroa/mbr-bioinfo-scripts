# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:36:40

from sys import argv, exit

help = """
Generates a GBX formatted key file from standard GBS keysfile.
No headers. Columns: sample, sequence of the barcode, name of the enzyme
        Name of enzyme = ApeKI
Usage ./gbsx_keys_generator.py <keyfile>
"""

try: argv[1]
except IndexError:
        print( help)
        exit()


enzyme = "ApeKI"

infile=open(argv[1],"r")
for line in infile:
        info=line.split("\t")
        sample=info[3]
        barcode=info[2]
        print( "{0}\t{1}\t{2}".format(sample,barcode,enzyme))