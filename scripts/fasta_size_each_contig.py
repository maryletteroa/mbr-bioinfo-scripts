#!/usr/bin/env python

'''
Marylette B. Roa
@MaryletteRoa
4-September-2017
'''

try:
    argv[1]
except IndexError:
    help = './foo.py <contings.fasta>'
    print(help)
    exit()



lens = {}
with open(argv[1]) as inf:
    lines = inf.readlines()
    for line in lines:
        if line.startswith('>'):
            print(line)
        else:
            pass

