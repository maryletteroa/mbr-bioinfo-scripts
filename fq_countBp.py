#!/usr/bin/env python

from sys import argv, exit

try: argv[1]
except IndexError:
   print()
   print()
   print('foo.py <fq> [fq] ..')
   exit()


def countbp(file_):
   lens = 0
   with open(file_) as inf:
     for i, line in enumerate(inf.readlines()):
        if i % 4 == 1:
           lens = lens + len(line.strip())
   return(lens)


fqs = argv[1:]
lens = 0
for fq in fqs: 
   lens = lens + countbp(fq)

print(lens)
