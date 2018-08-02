# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-07-09 17:03:01
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-08-02 18:21:49



#  grep 'ANNOTATED' blast2go_go_table_20180709_1217.txt | grep 'structural constituent of ribosome' | rev | cut -f 6 | rev > gos.txt

from sys import argv, exit
import os

script_name = os.path.basename(__file__)

try:
	blast2go_tsv = argv[1]
except IndexError:
	help = f'{script_name} <blast2go.tsv>'
	print(help)
	exit()

gos = []
with open(blast2go_tsv) as inf:
    for line in inf.readlines()[1:]:
        if 'MAPPED' in line:
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



