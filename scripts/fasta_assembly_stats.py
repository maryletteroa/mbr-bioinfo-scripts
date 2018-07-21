# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-07-09 13:16:12
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-19 10:44:04


from sys import argv, exit
from statistics import mean, median, mode

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
mean_len = mean(seqlen_list)
median_len = median(seqlen_list)
mode_len = mode(seqlen_list)
num_len = len(seqlen_list)
total_len = sum(seqlen_list)

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

print("N50,Mean,Median,Mode,Num_contigs,Largest_contig,TotalAssemblySize")
print(f'{N50},{mean_len},{median_len},{mode_len},{num_len},{largestContigLen},{total_len}')
