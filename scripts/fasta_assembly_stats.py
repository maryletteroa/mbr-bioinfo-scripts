#!/usr/bin/env python
'''
@MaryletteRoa
#===============================================================================
# script calculates N50 value for assembly, only calculate for contigs >= 500bp
#===============================================================================
'''

from sys import argv, exit

try:
	contigsMultifasta, length_filter = argv[1], argv[2]
except IndexError:
	print('foo.py <assembly.contigs.fasta> <cutoff bp>')
	exit()
#header = argv[2]

contigsLength = []
seqlen_list = []
Sum = 0
from Bio import SeqIO
for seq_record in SeqIO.parse(open(contigsMultifasta), "fasta"):
    seqlen = len(seq_record.seq)
    if seqlen >= int(length_filter):
       seqlen_list.append(seqlen)
       Sum += len(seq_record.seq)
       contigsLength.append(len(seq_record.seq))

largestContigLen=max(seqlen_list)

teoN50 = Sum / 2.0
contigsLength.sort()
contigsLength.reverse()

#checking N50
testSum = 0
N50 = 0
for con in contigsLength:
    testSum += con
    if teoN50 < testSum:
        N50 = con
        break

print "N50,Num_contigs,Largest_contig,TotalAssemblySize"
print "{0},{1},{2},{3}".format(str(N50),str(len(contigsLength)),str(largestContigLen),str(sum(seqlen_list)))
