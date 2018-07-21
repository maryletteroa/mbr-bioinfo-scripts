# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:29:00


from sys import argv, exit
import os

script_name = os.path.basename(__file__)

try: argv[1]
except IndexError:
   print("Outputs min, max, and average alignment coverage")
   print(f"Usage: {script_name} <sample.cov>")
   print("   <sample.cov> is samtools depth output")
   exit()

covs = []
with open(argv[1]) as inf:
    lines = inf.readlines()
    for line in lines:
       ref, pos, cov = line.split()
       covs.append(int(cov.strip()))

average = float(sum(covs))/len(covs)

print("lowest: {}, highest: {}, average: {}".format(min(covs),max(covs), round(average,2)))
