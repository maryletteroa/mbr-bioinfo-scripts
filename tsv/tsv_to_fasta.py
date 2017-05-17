#!/usr/bin/env python
'''
@MaryletteRoa
'''

from sys import argv, exit

try:
	argv[1]
except IndexError:
	print('foo.py <tsv>')
	print('  col1: header, col2: sequence')
	exit()

infile=open(argv[1],"r").readlines()
for line in infile:
        info=line.split("\t")
        header=info[0]
        sequence=info[1].strip("\n")
        fasta=">{header}\n{sequence}".format(header=header,sequence=sequence)
        print(fasta)