# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:36:14

import sys
sys.path.append('/mnt/e/virtual_envs/windowsEnv/lib/python3.4/site-packages')

from Bio import SeqIO
import argparse

parser=argparse.ArgumentParser(description="Converts fastq file to a fasta file.")
parser.add_argument("input", help="input file in .fastq format")
parser.add_argument("output", help="output fasta file")
args=parser.parse_args()

#main

fastq_handle = open(args.input,"rU")
fastq_record = SeqIO.parse(fastq_handle,"fastq")
output = open(args.output,"w")
for record in fastq_record:
#       output.write(">"+record.name+"\n"+record.seq + '\n')
        string = f'>{record.name}\n{record.seq}\n'
        output.write(string)
output.close()
