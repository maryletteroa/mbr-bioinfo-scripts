# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:33:39


from sys import argv, exit

try: argv[1], argv[2], argv[3], argv[4]
except IndexError:
   help = '''foo.py <contigs.fa> <output_prefix> <organism> <strain> <plasmidStart>
      removes <200 bp contigs
      removes Ns at the start and end of contigs
   ouput: prefix.fsa'''
   print(help)
   exit()

headercount = 0
plasmidCounter = 0
outf = open(argv[2]+'.fsa','w')

organism = argv[3]
strain = argv[4]

with open(argv[1]) as contigsfile:
    contigs = contigsfile.read().split('>')[1:]
    if len(contigs) < 100: n=2
    elif len(contigs) >= 100: n=3
    for contig in contigs:
       header = contig.split('\n')[0]
       seqs = '\n'.join(contig.split('\n')[1:]).upper()
       if len(seqs) >= 200:
          seqs_strip = seqs.lstrip('N').rstrip('N')
          if len(seqs) > len(seqs_strip): print('contig {0} trimmed'.format(header))
          headercount += 1
          try:
             plasmidStart = argv[5]
             if headercount >= int(plasmidStart):
                plasmidCounter += 1
                contig='>contig{} [organism={}] [strain={}] [plasmid-name=unnamed{}]\n'.format(str(headercount).zfill(n), organism, strain, plasmidCounter)
             else: contig='>contig{} [organism={}] [strain={}]\n'.format(str(headercount).zfill(n), organism, strain)
          except IndexError: contig='>contig{} [organism={}] [strain={}]\n'.format(str(headercount).zfill(n), organism, strain)
          outf.write(contig)
          outf.write(seqs_strip)
       else: print('contig {0} less than <200 bp, removed'.format(header))