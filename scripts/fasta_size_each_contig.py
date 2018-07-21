# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:34:52

from sys import argv, exit

try:
    argv[1]
except IndexError:
    help = './foo.py <contigs.fasta>'
    print(help)
    exit()



sizes = {}
with open(argv[1]) as inf:
    lines = inf.readlines()
    for line in lines:
        if line.startswith('>'):
            header = line.strip('\n').split('>')[1]
            if header not in sizes:
                sizes[header] = 0
        else:
            size = len(line.strip('\n'))
            sizes[header] = size

print('<header>:<size in bp>')
for header in sizes:
    size = sizes[header]
    print(f'{header}:{size}')

