# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:32:21


from sys import argv,exit
from Bio import SeqIO
from statistics import mean, median, mode

try: inf=open(argv[1])
except IndexError:
   print("Counts length of multiFa")
   print("./foo.py <seq.fa> [each]")
   exit()

reads=SeqIO.parse(inf,"fasta")
lengths = []
for read in reads:
    length = len(read.seq)
    lengths.append(length)
    if 'each' in argv:
        print(f'{read.description}: {length}')
    else:
        pass

print(f'Mean: {mean(lengths)}')
print(f'Median: {median(lengths)}')
print(f'Mode: {mode(lengths)}')
print(f'Mean - Max: {min(lengths)} - {max(lengths)}')
print(f'Total: {sum(lengths)}')


