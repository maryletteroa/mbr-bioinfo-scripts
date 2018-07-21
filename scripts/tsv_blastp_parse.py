# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:37:52

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
