#!/usr/bin/env python
'''
@MaryletteRoa
'''

from sys import argv, exit

help = """
Generates a GBX formatted key file from standard GBS keysfile.
No headers. Columns: SampleName, code,paired,file
        Paired = p
Usage: foo.py <barcode_file> <name_of_gbs_seq>
"""

try: argv[1], argv[2]
except IndexError:
        print help
        exit()

print "SampleName\tcode\tpaired\tfile"
infile=open(argv[1],"r").readlines()[1:]
for line in infile:
        info=line.split("\t")
        barcode=info[2]
        sample=info[3]
        print "{0}\t{1}\t{2}\t{3}".format(sample,barcode,"p",argv[2])