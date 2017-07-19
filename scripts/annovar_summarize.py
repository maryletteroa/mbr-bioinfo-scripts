#!/usr/bin/env python
'''
@MaryletteRoa
'''

from sys import argv

infile=open(argv[1])
outfile=open(argv[1].rstrip("txt")+"summ.txt","w")
fileNum=argv[1].split("/")[-1].split("_")[0]
headers="Sample\tStart\tEnd\tRef\tAlt\tFunc.refGene\tGene.refGene\tGeneDetail.refGene\tExonicFunc.refGene\tAAChange.refGene\tsnp144\tGenotype\tAlleDepthRef\tAlleDepthAlt\tReadDepth\tSnpCallQuality\tGenotypeCallQuality\n"
outfile.write(headers)
for line in infile.readlines()[1:]:
        info=line.split("\t")
        annotDetails = "\t".join(info[1:11])
        snpQuality = info[12]
        snpDetails=info[23].strip("\n").split(":")
        gt = snpDetails[0]
        adRef = snpDetails[1].split(",")[0]
        adAlt = snpDetails[1].split(",")[1]
        dpRef = snpDetails[2]
        gq = snpDetails[3]
        printString = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\n".format(fileNum,annotDetails,gt,adRef,adAlt,dpRef,snpQuality,gq)
        outfile.write(printString)
infile.close()
outfile.close()