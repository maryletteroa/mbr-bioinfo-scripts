# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:33:44


from sys import argv, exit
try:
   inf = argv[1]
   pairnum = argv[2]
except IndexError:
   print("Formats illumina fastqs with /1 or /2 in headers of PE reads")
   print("Req: <sample.fq> <1|2>")
   exit()

outf = open(inf+".reformatted.fq","w")
with open(argv[1]) as fq:
    for i,j in enumerate(fq.readlines()):
       if i%4 ==0:
           header = " ".join(j.split(" ")[0:-1]) + "/{}".format(pairnum)+"\n"
           outf.write(header)
       else: outf.write(j)
outf.close()
