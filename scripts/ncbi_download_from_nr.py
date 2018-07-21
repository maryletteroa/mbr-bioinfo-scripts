# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:37:00

import sys

from Bio import Entrez
from Bio import SeqIO
from os import system
from sys import argv, exit

Entrez.email='hello@world.com' #required for Entrez

try: 
    openFiltered=open(argv[1])
except IndexError:
    help = './ncbi_download_fron_nr.py <sequence.gi.txt>'
    print(help)
    exit()


allData = openFiltered.readlines()

giNums = [data.strip() for data in allData]

stopIter = 0
loopIndex = 0

#download 100 records at a time
while stopIter < len(giNums):
    print("Downloading {0}/{1}".format(stopIter+1,len(giNums)))
    downloadFasta = Entrez.efetch(db="protein", rettype="fasta", id="{0}".format(",".join(index for index in giNums[stopIter:stopIter+100])))
    
    outputFasta = open("sequence_{0}.fasta".format(loopIndex),'w') #output directory
    outputFasta.write(downloadFasta.read()) #this is how you read/write directly from Entrez download
    
    stopIter = stopIter + 100
    loopIndex = loopIndex + 1

outputFasta.close()
print("Downloaded {0}/{0}".format(len(giNums),len(giNums)))

#concatenate metafiles into a single file
print("Writing into one multi-FASTA file.")
system("cat sequence_*.fasta > sequence.fasta")

#delete metafiles
system("rm sequence_*.fasta")

print( "Done.")
