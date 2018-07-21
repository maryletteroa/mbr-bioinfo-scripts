# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-09 13:02:16
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:38:13

import requests
from sys import argv, exit
from os import system

try:
    accessions = argv[1]
except IndexError:
    about = '''
Script to download a list of ENSEMBL accession numbers (equivalent to NCBI Gene DB)
corresponding to LOCUS ids from the Uniprot website using the REST API of uniprot
'''
    help = f'{argv[0].split("/")[-1]} <accessions.txt>'
    print(help)
    exit()

with open(accessions) as f:
    acc_ids = [a.strip() for a in f.readlines()]

total = len(acc_ids)
sl = 100
for r in range(0,total,sl):
    query = ' OR '.join(acc_ids[r:r+sl])
    print(f'Downloading {r}/{total}')
    url = f'https://www.uniprot.org/uniprot/?query={query}&format=fasta'
    req = requests.get(url, allow_redirects=True)
    open(f'sequence.{r}.fasta', 'wb').write(req.content)

print('Writing into one multi-FASTA file.')
system('cat sequence_*.fasta > sequence.fasta')
system('rm sequence_*.fasta')
print('Done')

## https://www.uniprot.org/uniprot/?query=Zm00001d053895%20OR%20Zm00001d053899&format=fasta
