#!/usr/bin/python
'''
@MaryletteRoa
'''

import sys
sys.path.append('/mnt/e/virtual_envs/windowsEnv/lib/python3.4/site-packages')


from Bio import SeqIO
from BCBio import GFF

in_file = "sequence.gb"
out_file = "sequence.gff"
in_handle = open(in_file)
out_handle = open(out_file, "w")

GFF.write(SeqIO.parse(in_handle, "genbank"), out_handle)

in_handle.close()
out_handle.close()