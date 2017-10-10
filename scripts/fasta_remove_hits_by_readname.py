#!/usr/bin/env python
#date: 22 August 2017

'''
@MaryletteRoa
'''

from sys import argv, exit
from Bio import SeqIO

"""
Input:
(1) Text file with list of contigs headers, newline separated
(2) Assembly contigs.fasta
"""

help="""
Removes reads from a multi-FASTA file using a list of headers. Outputs in STDOUT.
Usage:\n./foo.py <headers> <contigs.fasta>
    headers, text file with list of contigs headers newline separated
    contigs.fasta, assembly file in FASTA format
"""

try:
    nodenames=argv[1]
    assembly=argv[2]
except IndexError:
    print(help)
    exit()

def seqdict(filename):
    seqdict={}
    assembly=open(filename,"r")
    seqs=SeqIO.parse(assembly,"fasta")
    for seq in seqs:
        seqdict[seq.description]=seq.seq
    return seqdict



#main
assemblydict=seqdict(assembly)
infile=open(nodenames,"r").readlines()
headers = []

for line in infile:
    header=line.strip("\n")
    headers.append(header)

for key in assemblydict:
    if key not in headers:
        try: print(">{0}\n{1}\n".format(key,assemblydict[key]))
        except KeyError:
           pass
