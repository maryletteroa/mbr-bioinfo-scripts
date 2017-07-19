#!/usr/bin/env python
'''
@MaryletteRoa
Splits fastq files in smaller chuncks
- could be improved
'''
from sys import argv, exit

try:
   # the number of splits 
   num_split = int(argv[1])
   # input as many fastqs as you like
   fastqs = argv[2:]
except IndexError:
   print('foo.py <number of splits> <fastq> [fastq .. ]')
   exit()

for fastq in fastqs:
   infile = open(fastq).readlines()

   lines_count = len(infile)
   reads_in_split = lines_count / 4 / num_split
   lines_in_split = reads_in_split * 4

   indices = range(0,lines_count,lines_in_split)

   counter = 1
   for i,j in enumerate(indices[0:num_split-1]):
      name = "sub"+str(counter)+"_"+fastq.split(".")[0]+".fastq"
      outfile = open(name,"w")
      print >> outfile, "".join(infile[j:indices[i+1]]).strip("\n")
#      print j, indices[i+1]
      outfile.close()
      counter = counter + 1
   name = "sub"+str(counter)+"_"+fastq.split(".")[0]+".fastq"
   outfile = open(name,"w")
   print >> outfile, "".join(infile[indices[num_split-1]:]).strip("\n")
#   print indices[num_split]
   outfile.close()
