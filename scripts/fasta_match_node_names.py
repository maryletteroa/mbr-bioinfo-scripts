# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:33:42


from sys import argv, exit
from Bio import SeqIO

"""
Input:
(1) Text file with list of contigs headers, newline separated
(2) Assembly contigs.fasta
"""

help="""
Subsets a multi-FASTA file using a list of headers. Outputs the subset in STDOUT.
Usage:\n./match_node_names.py <headers> <contigs.fasta>
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

for line in infile:
    key=line.strip("\n")
    try: print(">{0}\n{1}".format(key,assemblydict[key]))
    except KeyError:
        # print("{} NOT FOUND".format(key))
        pass
