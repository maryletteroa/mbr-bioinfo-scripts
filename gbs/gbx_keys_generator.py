#!/usr/bin/env python
'''
@MaryletteRoa
'''

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