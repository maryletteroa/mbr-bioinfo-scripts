#!/usr/bin/env python

'''
@MaryletteRoa
11-April-2016
'''

from sys import argv, exit

try: argv[1], argv[2]
except IndexError:
        print( """
        Usage: pair_reads.py <read1.fq> <read2.fq>
        
        Note: Requires that the headers of the two reads file are the same
        Outputs: <reads1/2>_pair.fq, <reads1/2>_single.fq
        """)
        exit()


reads1 = {}
reads2 = {}
pair1 = open("".join(argv[1].split(".")[0:-1])+"_pair.fq","w")
pair2 = open("".join(argv[2].split(".")[0:-1])+"_pair.fq","w")
single1 = open("".join(argv[1].split(".")[0:-1])+"_single.fq","w")
single2 = open("".join(argv[2].split(".")[0:-1])+"_single.fq","w")


with open(argv[1]) as fq1:
        data1 = fq1.readlines()
        for i,j in enumerate(data1):
                if i % 4 == 0:
                        header = j.strip("\n")
                        reads1[header] = data1[i:i+4]

#print reads1["@Frag_175976 sequence (Strand - Offset 2216498--2216734)  151M"]

with open(argv[2]) as fq2:
        data2 = fq2.readlines()
        for i,j in enumerate(data2):
                if i % 4 == 0:
                        header = j.strip("\n")
                        reads2[header] = data2[i:i+4]
                        if header in reads1:
                                pair1.write("".join(reads1[header]).strip("\n") + '\n')
                                pair2.write("".join(reads2[header]).strip("\n") + '\n')
                        else: single2.write("".join(reads2[header]).strip("\n") + '\n')


with open(argv[1]) as fq1:
        data1 = fq1.readlines()
        for i,j in enumerate(data1):
                if i % 4 == 0:
                        header = j.strip("\n")
                        if header not in reads2: print >> single1.write("".join(reads1[header]).strip("\n") + '\n')

pair1.close()
pair2.close()
single1.close()
single2.close()