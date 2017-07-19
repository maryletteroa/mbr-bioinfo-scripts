#!/usr/bin/env python
'''
@MaryletteRoa
'''

from sys import argv, exit
try: argv[1], argv[2]
except IndexError:
    print()
    print('foop.py <blastp.tab> <sample name or tag>')
    print('-outfmt 6  qseqid sseqid stitle pident qlen slen length qstart qend sstart send evalue bitscore qcovs qcovhsp')
    exit()

print('sample\tqseqid\tstitle\tpident\tqcovhsp\tevalue')
with open(argv[1]) as tab:
    lines = tab.readlines()
    for line in lines:
       qseqid, sseqid, stitle, pident, qlen, slen, length, qstart, qend, sstart, send, evalue, bitscore, qcovs, qcovhsp = line.strip().split('\t')
       print('{}\t{}\t{}\t{}\t{}\t{}'.format(argv[2],qseqid, stitle, pident, qcovhsp, evalue))
