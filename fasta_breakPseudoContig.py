#!/usr/bin/env python


from sys import argv, exit

try: argv[1]
except IndexError:
   print('foo.py <pseudocontig.fsa>')
   print()
   print('  breaks Contiguator pseudocontig at consecutive 100Ns')
   exit()

with open(argv[1]) as inf:
   infs= inf.read().split('\n')
   header = infs[0]
   sequence = ''.join(infs[1:])
   countNs = sequence.count('N'*100)
   split_sequences = '\n>contig\n'.join(sequence.split('N'*100))
   print('>contig')

   print(split_sequences)