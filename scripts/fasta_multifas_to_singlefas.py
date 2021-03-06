# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:33:41


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