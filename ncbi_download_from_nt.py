#! /usr/bin/env python
'''
@MaryletteRoa
! needs more work on this script
'''

import sys
sys.path.append('/mnt/e/virtual_envs/windowsEnv/lib/python3.4/site-packages')

from Bio import Entrez
from Bio import SeqIO
from os import system
from sys import argv

Entrez.email='hello@world.com' #required for Entrez

openFiltered=open("filtered.csv")


allData = openFiltered.readlines()

giNums =  allData[1].split(';')[0]

for num in range(2,len(allData)):
	giNums = giNums + ',' + allData[num].split(';')[0]

giNums = giNums.split(',')


stopIter = 0
loopIndex = 0

#download 100 records at a time
while stopIter < len(giNums):
	print "Downloading {0}/{1}".format(stopIter+1,len(giNums))
	downloadFasta = Entrez.efetch(db="nucleotide", rettype="fasta", id="{0}".format(",".join(index for index in giNums[stopIter:stopIter+100])))
	
	outputFasta = open("sequence_{0}.fasta".format(loopIndex),'w') #output directory
	output.write(FastadownloadFasta.read() + '\n') #this is how you read/write directly from Entrez download
	
	stopIter = stopIter + 100
	loopIndex = loopIndex + 1

outputFasta.close()
print "Downloaded {0}/{0}".format(len(giNums),len(giNums))

#concatenate metafiles into a single file
print "Writing into one multi-FASTA file."
system("cat sequence_*.fasta > sequence.fasta")

#delete metafiles
system("rm sequence_*.fasta")

print "Done."
