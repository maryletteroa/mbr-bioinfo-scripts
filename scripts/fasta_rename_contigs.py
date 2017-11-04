#!/usr/bin/env python3.6

# -*- coding: utf-8 -*-
# @Author: Marylette Roa
# @Date:   2017-11-04 16:12:26
# @Last Modified by:   Marylette Roa
# @Last Modified time: 2017-11-04 16:17:47



from sys import argv, exit

try:
    fasta_file = argv[1]
except IndexError:
    help = 'foo.py <contigs.fa>'
    print(help)
    exit()

headercount = 0
outf_name = '.'.join(argv[1].split('.')[0:-1])  + '.renamed.fasta'
outf = open(outf_name,'w')

with open(fasta_file) as inf:
    sequences = [line for line in inf.read().split('>')[1:]]
    fastas = {sequence.split('\n')[0]:''.join(sequence.split('\n')[1:]).upper() for sequence in sequences}

counter = 0
for fasta in fastas:
    counter += 0
    header = 'contig_{counter}'
    sequence = fastas[fasta]
    fasta_p = f'>{header}\n{sequence}'
    print(fasta_p, file=outf, end='\n')

print(f'Output: {outf_name}')
outf.close()

