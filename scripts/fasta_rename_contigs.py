#!/usr/bin/env python3.6

# -*- coding: utf-8 -*-
# @Author: Marylette Roa
# @Date:   2017-11-04 16:12:26
# @Last Modified by:   Marylette Roa
# @Last Modified time: 2017-11-04 16:33:55



from sys import argv, exit

try:
    fasta_file = argv[1]
except IndexError:
    help = 'foo.py <contigs.fa>'
    print(help)
    exit()


with open(fasta_file) as inf:
    sequences = [line for line in inf.read().split('>')[1:]]
    fastas = {sequence.split('\n')[0]:''.join(sequence.split('\n')[1:]).upper() for sequence in sequences}


outf_name = '.'.join(argv[1].split('.')[0:-1])  + '.renamed.fasta'
outf = open(outf_name,'w')

map_outf_name = 'map.txt'
map_outf = open(f'{map_outf_name}','w')

counter = 0
for fasta in fastas:
    counter += 1
    header = f'contig_{counter}'
    sequence = fastas[fasta]
    fasta_p = f'>{header}\n{sequence}'
    map_p = f'{fasta}\t{header}'
    print(fasta_p, file=outf, end='\n')
    print(map_p, file=map_outf, end='\n')

print(f'Output: {outf_name}, {map_outf_name}')
outf.close()

