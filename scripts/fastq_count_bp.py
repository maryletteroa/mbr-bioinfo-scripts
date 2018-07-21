# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:35:22

'''
Counts the bp in fastq files
Produces a total count of all fastq supplied
'''

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
