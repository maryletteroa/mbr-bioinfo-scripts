# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-09 13:02:16
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:31:12

from sys import argv, exit
from Bio import SeqIO


try:
    fasta_file = argv[1]
except IndexError:
    about = '''
Converts embl file to fasta
'''
    usage = f'''
Usage: {argv[0].split('/')[-1]} <sequence.embl>
'''
    help = f'{about}{usage}'
    print(help)
    exit()


outname = f'{fasta_file}.fasta'
outf = open(outname,'w')

with open(fasta_file) as inf:
    for record in SeqIO.parse(inf, 'embl'):
        header = record.id
        sequence = record.seq
        fasta = f'>{header}\n{sequence}'
        print(fasta,file=outf)
outf.close()


print(f'Output: {outname}')
