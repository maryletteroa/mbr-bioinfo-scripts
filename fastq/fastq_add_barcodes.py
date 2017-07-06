#!/usr/bin/env python

'''
@MaryletteRoa
6-July-2017
'''

from sys import argv, exit

try:
    fastq = argv[1]
    barcode = argv[2]
    prefix = argv[3]
except IndexError:
    about = 'Changes the headers of miseq fastq files, last character to specified barcode'
    help = f'foo.py <in.fastq> <barcode> <out.prefix>'
    print(about)
    print(help)
    exit()


outf = open(f'{prefix}.barcode.fastq','w')

line_counter = 0
with open(argv[1]) as inf:
    for line in inf:
        line_counter += 1
        if line_counter % 4 == 1:
            header = line.strip()[:-1] + barcode
            outf.write(header+'\n')
        else:
            outf.write(line)