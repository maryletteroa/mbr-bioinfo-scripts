# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:33:45


from sys import argv,exit

try:
   fasta,prefix,cutoff=argv[1],argv[2],argv[3]
except IndexError:
   print("Filters sequences based on length")
   print("./filterAssembly.py <seq.fa> <prefix> <len>")
   exit()

passed= open("{0}.filt{1}.fa".format(prefix,cutoff),"w")
failed= open("{0}.failed.fa".format(prefix,cutoff),"w")

with open(fasta) as inf:
   reads = inf.read().split(">")[1:]
   for read in reads:
      desc = read.split("\n")[0]
      seqs = "".join(read.split("\n")[1:])
      if len(seqs) >= int(cutoff): passed.write(">{0}\n{1}\n".format(desc,seqs))
      else: failed.write(">{0}\n{1}\n".format(desc,seqs))
passed.close()
failed.close()
