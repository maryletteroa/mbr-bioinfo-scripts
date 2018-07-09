#!/usr/bin/env python
from sys import argv, exit
import statistics

try:
    fasta = argv[1]
except IndexError:
    about = '''Outputs %GC per contig. Calculates only over ATGC characters. 
    Non-ATGC are not counted in the overall length of the sequence.
    Python3.6.x syntax.'''
    usage = '\nfoo.py <seq.fasta> [summary]'
    print(about)
    print(usage)
    exit()

all_gc = []
skip = 0
with open(fasta) as inf:
    records = inf.read().split('>')[1:]
    for record in records:
        header = record.split('\n')[0]
        seq = ''.join(record.split('\n')[1:]).upper()
        at = seq.count('A') + seq.count('T')
        gc = seq.count('G') + seq.count('C')
        length = gc + at
        try:
            prec_gc = (gc / length) * 100.0
            all_gc.append(prec_gc)
            if 'summary' not in argv: print(f'{header}\t{round(prec_gc,2)}')
        except ZeroDivisionError:
            print(header,seq)
            skip += 1

mean = statistics.mean(all_gc)
median = statistics.median(all_gc)
mode = statistics.mode(all_gc)

print(f'Mean: {mean}, Median: {median}, Mode: {mode}')
print(f'Skipped over {skip} sequences due to ZeroDivision')

