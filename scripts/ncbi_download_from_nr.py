#!/usr/bin/env python
'''
@MaryletteRoa
'''

import sys
sys.path.append('/mnt/e/virtual_envs/windowsEnv/lib/python3.4/site-packages')

from Bio import Entrez, SeqIO
Entrez.email = "hello@world.com"

gi_file=open("sequence.gi.txt")
for gi_num in gi_file:
        handle = Entrez.efetch(db="protein", id=gi_num.strip(), rettype="fasta", retmode="text")
        record = SeqIO.read(handle, "fasta")
        handle.close()
        string = ">{description}\n{sequence}".format(description=record.description, sequence=record.seq)
        print(string)