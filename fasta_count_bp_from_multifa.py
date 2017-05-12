#!/usr/bin/env python
'''
@MaryletteRoa
'''

from sys import argv,exit
from Bio import SeqIO
try: inf=open(argv[1])
except IndexError:
   print("Counts length of multiFa")
   print("./foo.py <seq.fa>")
   exit()
reads=SeqIO.parse(inf,"fasta")
seqlen=0
for read in reads: seqlen=seqlen+len(read.seq)
print(seqlen)
