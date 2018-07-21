# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:38:34


from sys import argv,exit
try: vcf,dp_cutoff,prefix=argv[1],argv[2],argv[3]
except IndexError:
  print("Filter vcf based on depth of coverage, and SNPs only")
  print("@maryletteroa")
  print("./foo.py <sample.vcf> <dp_cutoff> <prefix>")
  exit()

passed = open("{0}.passed{1}.vcf".format(prefix,dp_cutoff),"w")
failed = open("{0}.failed{1}.vcf".format(prefix,dp_cutoff),"w")
with open(vcf) as inf:
  lines = inf.readlines()
  for line in lines:
     if line.startswith("#") == False:
        info=line.split("\t")[7]
        dp = info.split("DP=")[1].split(";")[0]
        ref = line.split("\t")[3]
        alt = line.split("\t")[4]
        if int(dp) >= int(dp_cutoff):
           passed.write(line)
        else:
           failed.write(line)
     else: 
        passed.write(line)
        failed.write(line)

passed.close()
failed.close()
