# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:36:31

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