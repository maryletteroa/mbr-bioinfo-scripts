#!/usr/bin/python

'''
@MaryletteRoa
7 March 2017
'''

from sys import argv
from Bio.Blast import NCBIXML

blast = NCBIXML.parse(open(argv[1]))
outf = open('hspQseq.faa','w')

for record in blast:
   query_title = record.query
   if record.alignments:
      for recHit in record.alignments:
         for hsp in recHit.hsps:
           start = hsp.query_start
           end = hsp.query_end
           query_seq = hsp.query.replace('-','')
           hit_title = recHit.title
           title = f'Query: {query_title} Hit: {hit_title}'
           fas_header = '>{}_{}_{}'.format(title,start,end)
           fasta = '{}\n{}'.format(fas_header,query_seq)
           outf.write(fasta+'\n')
         break

outf.close()
blast.close()
