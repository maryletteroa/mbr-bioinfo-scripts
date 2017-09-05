#!/usr/bin/env python
'''
@MaryletteRoa
'''

from sys import argv,exit
from Bio import SeqIO
try: inf=open(argv[1])
except IndexError:
   print("Counts length of multiFa")
   print("./foo.py <seq.fa> [each]")
   exit()
reads=SeqIO.parse(inf,"fasta")
seqlen=0
for read in reads:
    length = len(read.seq)
    seqlen=seqlen+length
    if 'each' in argv:
        print(read.description + ':' + length)
    else:
        pass
print('total assembly size:' + seqlen)


