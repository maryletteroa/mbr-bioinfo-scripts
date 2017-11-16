#!/usr/bin/env python3.6 

# -*- coding: utf-8 -*-
# @Author: marylette
# @Date:   2017-11-16 12:31:26
# @Last Modified by:   marylette
# @Last Modified time: 2017-11-16 12:30:19


from sys import argv, exit


def break_fasta(fasta_file,num_contigs):
    with open(fasta_file) as inf:
        mult_fasta = [line for line in inf.read().split('>')[1:]]
    num_seqs = len(mult_fasta)
    for num in range(0,num_seqs,num_contigs):
        yield(mult_fasta[num:num+50])


def main():
    for i,chunk in enumerate(break_fasta(fasta_file, num_contigs)):
        prefix = '.'.join(fasta_file.split('.')[:-1])
        outf_name = f'{prefix}.part{i+1:002}.fasta'
        outf = open(outf_name, 'w')
        str_chunk = '>'+'>'.join(chunk).strip()
        print(str_chunk, file=outf)
        print(f'Output: {outf_name}')



if __name__ == '__main__':
    try:
        fasta_file = argv[1]
        num_contigs = int(argv[2])
    except IndexError:
        help = f'./fasta_break_multifasta_by_num_contigs.py <seq.fasta> <num_contigs>'
        print(help)
        exit()
    main()