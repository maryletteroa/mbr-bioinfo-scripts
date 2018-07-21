# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:35:52

from sys import argv, exit

try:
    fastqfile, readnames, outprefix = argv[1], argv[2], argv[3]
except IndexError:
    help='./foo.py <fastq> <readnames> <outprefix>\n readnames: newline delimited'
    print(help)
    exit()

print(f'Input fastq: {fastqfile}\nInput hits list: {readnames}')

line_counter = 0
reads = {}
with open(fastqfile) as inf:
    for line in inf:
        line_counter += 1
        if line_counter % 4 == 1:
            header = line.strip()[1:]
            reads[header] = ''
            rest = ''
        else:
            rest = rest + line
            if line_counter % 4 == 0:
                reads[header] = rest[:-1]

hits = []
with open(readnames) as inf2:
    for line in inf2.readlines():
        hits.append(line.strip('\n'))


outname = f'{outprefix}.filtered.fastq'
outf = open(f'{outname}','w')
for header in reads:
    if header not in hits:
        pstring = f'@{header}\n{reads[header]}\n'
        outf.write(pstring)

outf.close()

print(f'Filtered: {outname}')