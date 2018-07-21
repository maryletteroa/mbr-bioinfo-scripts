# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-07-21 08:53:23
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-21 09:21:25

'''
read tsv blast results to dictionary
collect reciprocal blast hits
inputs: two tsv
output: reciprocal hits
'''

from sys import argv
from os import path

try:
    blast_file1 = argv[1]
    blast_file2 = argv[2]
except IndexError:
    script_name = path.basename(__file__)
    about = '''Counts the number of reciprocal best hits between two BLAST tsv files.
    Query names should be first column, subject names second column'''
    usage = f'{script_name} <blast_file1> <blast_file2>'
    print(f'{about}\nUsage: {usage}')
    exit()


def get_hits(blast_file, index1, index2):
    with open(blast_file) as inf:
        results = {results.split()[index1]: results.split()[index2] for results in inf.readlines()}
        return(results)

results1 = get_hits(blast_file1, 0, 1)
results2 = get_hits(blast_file2, 1, 0)

count = 0
for query in results1:
    if query in results2:
        subject1, subject2 = (results1[query], results2[query])
        if subject1 == subject2:
            count += 1
print(count)