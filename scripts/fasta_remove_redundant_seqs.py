# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-09 13:02:16
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:33:36

from sys import argv,exit


try:
    fasta_file  = argv[1]
except IndexError:
    about = '''
Removes redundancy in fasta sequences (fasta sequences with completely identical characters) from a multi-fasta file.
Caution: Does not check for lettercases etc. Duplicate sequences are merged into one
'''
    usage = f'  Usage: {argv[0].split("/")[-1]} <sequence.fasta>'
    print(about, usage)
    exit()



with open(fasta_file) as inf:
    seqs = inf.read().split('>')[1:]

nrseqs = list(set(seqs))

nrseqs_out = ('>'+'>'.join(nrseqs))

outname = f'{fasta_file}.nrseqs.fasta'
fout = open(outname, 'w')
fout.write(nrseqs_out)
fout.close()

print(f'Output: {outname}')



