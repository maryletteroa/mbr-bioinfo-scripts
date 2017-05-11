#!/usr/bin/env python
'''
@MaryletteRoa
'''

from sys import argv, exit

try: argv[1]
except IndexError:
   print("Outputs min, max, and average alignment coverage")
   print("@maryletteroa")
   print("Usage: foo.py <sample.cov>")
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
