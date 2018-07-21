# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:35:01


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