# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:27:20

import os
from sys import argv
from Bio import SeqIO
from glob import glob


script_name = os.path.basename(__file__)
usage=f'''
Converts many ab1 sequences inside a directory to a single fastq file.
    <directory> - contains the files in ab1 extensions
    <out.fastq> - name of outfile
Usage: {script_name} <directory> <out.fastq>
'''

try:
        outfile = open(argv[2], 'w')
        outfile.write(ab1_to_fastq(argv[1]))
        outfile.close()
except IndexError: print(usage)

phred_ascii = {33:'!', 34:''', 35:'#', 36:'$', 37:'%', 38:'&', 
    39:''', 40:'(', 41:')', 42:'*', 43:'+', 44:',', 45:'-', 46:'0', 
    47:'/', 48:'0', 49:'1', 50:'2', 51:'3', 52:'4', 53:'5', 54:'6', 
    55:'7', 56:'8', 57:'9', 58:':', 59:';', 60:'<', 61:'=', 62:'>', 
    63:'?', 64:'@', 65:'A', 66:'B', 67:'C', 68:'D', 69:'E', 70:'F', 
    71:'G', 72:'H', 73:'I', 74:'J', 75:'K', 76:'L', 77:'M', 78:'N',
    79:'O', 80:'P', 81:'Q', 82:'R', 83:'S', 84:'T', 85:'U', 86:'V', 
    87:'W', 88:'X', 89:'Y', 90:'Z', 91:'[', 92:'\\', 93:']', 94:'^', 
    95:'_', 96:'`', 97:'a', 98:'b', 99:'c', 100:'d', 101:'e', 102:'f', 
    103:'g', 104:'h', 105:'i', 106:'j', 107:'k', 108:'l', 109:'m', 110:'n', 
    111:'o', 112:'p', 113:'q', 114:'r', 115:'s', 116:'t', 117:'u', 118:'v', 
    119:'w', 120:'x', 121:'y', 122:'z', 123:'{', 124:'|', 125:'}', 126:'~'}


def ab1_to_fastq(directory):
   fastq = []
   for ab1_file in glob(directory+'/*.ab1'):
      ab1 = open(ab1_file,'rb')
      sequence = SeqIO.read(ab1,'abi')
      ascii_quals = [phred_ascii[int(num_qual)+33] for num_qual in sequence.letter_annotations['phred_quality']]
      name = sequence.name
      seq = sequence.seq
      quality = ''.join(ascii_quals)
      fastq.append(f'@{name}\n{seq}\n+\n{quality}')
   return '\n'.join(fastq)

