# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:34:19

'''
Rename contigs by <tag># where # is consecutive
could be used to prepare contigs for NCBI submission
'''

from sys import argv, exit

try: argv[1], argv[2]
except IndexError:
   help = '''foo.py <contigs.fa> <output_prefix> [rename|ncbi_sub]
   use ncbi_sub if  the sequences are being preprocessed for ncbi wgs submission:
      removes <200 bp contigs
      removes Ns at the start and end of contigs
   ouput: prefix.fsa'''
   print(help)
   exit()

headercount = 0
outf = open(argv[2]+'.fsa','w')



with open(argv[1]) as contigsfile:
    contigs = contigsfile.read().split('>')[1:]
    if len(contigs) < 100: n=2
    elif len(contigs) >= 100: n=3
    for contig in contigs:
       header = contig.split('\n')[0]
       seqs = '\n'.join(contig.split('\n')[1:]).upper()
       if argv[3] == 'rename':
       	  headercount += 1
          outf.write('>contig{0}\n'.format(str(headercount).zfill(n)))
          outf.write(seqs+'\n')
       elif argv[3] == 'ncbi_sub':
          if len(seqs) >= 200:
          	seqs_strip = seqs.lstrip('N').rstrip('N')
          	if len(seqs) > len(seqs_strip): print('contig {0} trimmed'.format(header))
          	headercount += 1
          	contig='>contig{}\n'.format(str(headercount).zfill(n))
          	outf.write(contig)
          	outf.write(seqs_strip)
          else: print('contig {0} less than <200 bp, removed'.format(header))