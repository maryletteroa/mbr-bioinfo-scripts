#!/usr/bin/python

from Bio import SeqIO
from BCBio import GFF

in_file = "sequence.gb"
out_file = "sequence.gff"
in_handle = open(in_file)
out_handle = open(out_file, "w")

GFF.write(SeqIO.parse(in_handle, "genbank"), out_handle)

in_handle.close()
out_handle.close()