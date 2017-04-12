#!/usr/bin/env python 

from sys import argv,exit
try: fsa,prefix = argv[1],argv[2]
except IndexError:
   print("Cuts Pseudocontig (e.g. from CONTIGuator) at N's,generating a multifa file")
   print("@marylette")
   print("./cutFasAtN.py <seq.fasta> <prefix>")
   exit()

contigCounter = 0
outf=open("{0}.cut.fasta".format(prefix),"w")
with open(argv[1]) as inf:
   seqs = "".join([line.strip() for line in inf.readlines()[1:]])
#   print(seqs)
#   print(seqs.count("N"))
   contigs = seqs.split("N"*300)
   for contig in contigs:
     if contig != "": 
       contigCounter += 1
       outf.write(">{0}_scaff_{1:03d}\n".format(prefix,contigCounter))
       outf.write(contig+"\n")
outf.close()

