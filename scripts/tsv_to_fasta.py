# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:38:00

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