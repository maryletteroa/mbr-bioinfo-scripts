#!/usr/bin/env python3.6

# -*- coding: utf-8 -*-
# @Author: Marylette
# @Date:   2018-07-09 15:57:52
# @Last Modified by:   Marylette
# @Last Modified time: 2018-07-09 16:39:21


#  grep 'ANNOTATED' blast2go_go_table_20180709_1217.txt | grep 'structural constituent of ribosome' | rev | cut -f 6 | rev > gos.txt

from sys import argv, exit

try:
	blast2go_tsv = argv[1]
except IndexError:
	help = './blast2go_count_go.py <blast2go.tsv>'
	print(help)
	exit()

gos = []
with open(blast2go_tsv) as inf:
    for line in inf.readlines()[1:]:
        if 'ANNOTATED' in line:
            names =  line.strip().split('\t')[10]
            for go in names.split(';'):
                category = go.split(':')[0].lstrip()
                definition = go.split(':')[1]
                gos.append(f'{category}\t{definition}')

outn = 'go.count.txt'
outf = open(outn,'w')
for go in set(gos):
    print(f'{go}\t{gos.count(go)}',file=outf)
print(f'Result: {outn}')
outf.close()



