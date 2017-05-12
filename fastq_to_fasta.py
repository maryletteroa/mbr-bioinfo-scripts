#!/usr/bin/env python
'''
@MaryletteRoa
'''

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
	output.write(">"+record.name+"\n"+record.seq + '\n')