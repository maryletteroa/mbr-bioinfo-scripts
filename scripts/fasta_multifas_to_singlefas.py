#!/usr/bin/env python
'''
@MaryletteRoa
'''

from sys import argv, exit


try: argv[1], argv[2], argv[3]
except IndexError:
   print('foo.py <seq.fasta> <header> <prefix>.single.fas')
   print(' Combines multifastfile into one fasta file')
   exit()

outf = open(argv[3]+'.single.fasta','w')
outf.write('>'+argv[2]+'\n')
seqs = []
with open(argv[1]) as inf:
   for line in inf.readlines():
      if line.startswith('>'): pass
      else: seqs.append(line.strip())

full_seqs = ''.join(seqs)
for r in range(0,len(full_seqs),60):
    chunck = full_seqs[r:r+60]
    outf.write(chunck+'\n')
outf.close()