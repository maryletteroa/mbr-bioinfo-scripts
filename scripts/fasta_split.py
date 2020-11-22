# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2020-11-22 11:02:51
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2020-11-22 11:26:17


from sys import  argv, exit

try:
    inn = argv[1]
    num_files = argv[2]
    outn = argv[3]
except IndexError:
    print("<usage goes here>")
    exit()


file_counter = 0
with open(inn) as inf:
    fastas = inf.read().split(">")[1:]
    total_seqs = len(fastas)
    seq_per_file = total_seqs // int(num_files)
    for r in range(0, total_seqs, seq_per_file):
        file_counter +=1
        outn_ = f"{outn}_{file_counter}.fasta"
        outf = open(f"{outn_}", "w")
        # print(fastas[r:r+seq_per_file])
        sequences_to_file = ">"+">".join(fastas[r:r+seq_per_file]).rstrip()
        print(sequences_to_file, file=outf)
        print(f"Output: {outn_}")