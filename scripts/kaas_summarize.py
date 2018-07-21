#!/usr/bin/env python3.6

# -*- coding: utf-8 -*-
# @Author: Marylette
# @Date:   2018-07-10 09:12:14
# @Last Modified by:   Marylette
# @Last Modified time: 2018-07-21 12:43:00

from sys import argv, exit

try:
    keg_file = argv[1]
except IndexError:
    help = './kass_count_cds.py <q00001.keg>'
    print(help)
    exit()


## construct dictionary
#kegs = {'A': {'B': {'C': {'D': [] }}}}
kegs = {}

symbs = ('#','!','+')

with open(keg_file) as inf:
    for line in inf.readlines():
        if not line.startswith(symbs):
            if line.startswith('A'):
                cds = []
                a_cat = line.strip()
                kegs[a_cat] = {}
            elif line.startswith('B'):
                if line[1]  != '\n':
                    b_cat = 'B'+' '.join(line.strip().split(' ')[2:])
                    kegs[a_cat][b_cat] = {}
            elif line.startswith('C'):
                c_cat = 'C'+' '.join(line.strip().split(' ')[4:])
                kegs[a_cat][b_cat][c_cat] = []
            else:
                ctg = ' '.join(line.strip().split(' ')[6:])
                kegs[a_cat][b_cat][c_cat].append(ctg)

outn = 'kaas_summary.txt'
outf = open(outn,'w')

for k1 in kegs.keys():
    for k2 in kegs[k1].keys():
        for k3 in kegs[k1][k2].keys():
            cdss = kegs[k1][k2][k3]
            num_cds = len(cdss)
            if num_cds != 0: ## do not consider categories without contig assignments
                for cds in cdss:
                    cds_name = cds.split(';')[0]
                    function = ';'.join(cds.split(';')[1:])
                    outp = '\t'.join([cds_name, k1, k2, k3, function])
                    print(outp, file=outf)
print(f'Results: {outn}')
outf.close()