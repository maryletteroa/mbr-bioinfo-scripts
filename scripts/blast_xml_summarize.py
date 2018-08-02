# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-08-02 10:12:35
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-08-02 14:06:48

'''
Authors note:
- Parsing xml as text now because I just want to use core python libraries
- Code could be written more beautifully, feel free
'''

from sys import argv, exit
import os
import re

try: 
    blastxml = argv[1]
except IndexError:
    usage = f'{os.path.basename(__file__)} <blast.xml>'
    print(usage)
    exit()


def count_ranges(ranges, nums_list,evals=False):
    total = 0
    for ran in ranges:
        count = 0
        for num in nums_list:
            if evals:
                try:
                    if num > ran[0] and num <= ran[1]:
                        count += 1
                except TypeError:
                    if num == ran:
                        count += 1
            else:
                try:
                    if num >= ran[0] and num < ran[1]:
                        count += 1
                except TypeError:
                    if num >= ran:
                        count += 1
        total += count
        print(ran, count)
    return(total)


def check(list, total):
        if len(list) == total:
            print('total', total)
            print('hits matched total: \033[92m OK \x1b[0m')
        else: print('hits did not match total, check your ranges: \033[91m FAIL \x1b[0m')


def summ_evalue(blastxml):
    print('--- EVALUE ---')
    with open(blastxml) as inf:
        evalues = [float(line.split('>')[1].split('<')[0]) for line in inf.readlines() if 'Hsp_evalue' in line]

    ranges = [(0), (0,1e-300), (1e-300, 1e-200), (1e-200,1e-100), (1e-100,1e-50), (1e-50,1e-5)]
    # ranges = [(0),(0,1e-300), (1e-300,1e-200), (1e-200, 1e-100), (1e-100, 1e-50), (1e-50, 1e-5)]

    total = count_ranges(ranges, evalues, evals=True)

    check(evalues, total)


def summ_tax(blastxml):
    with open(blastxml) as inf:
        print('--- TAXONOMY ---')

        ## get the last value [-1] since some non-species related info are also written inside brackets
        taxs = [line.split(']<')[0].split('[')[-1] if 'Hit_def' not in line.split(']<')[0].split('[')[-1] else "Unknown species" \
                for line in inf.readlines() if '/Hit_def' in line]        
        
        tax_counts = [(tax, taxs.count(tax)) for tax in set(taxs)]
        
        sorted_tx = sorted(tax_counts, key = lambda x: x[1], reverse=True)
        top, others = sorted_tx[:5], sorted_tx[5:]
        sum_others = sum(map(lambda x: x[1], others))

        total = 0
        for t in top:
            print(t[0], t[1])
            total += t[1]
        print('Others', sum_others)
        total += sum_others

        check(taxs, total)



def summ_hits_by_len(blastxml):
    print('--- LENGHTS (1st: hits, next: without hits) ---')
    with open(blastxml) as inf:
        iterations = [iteration for iteration in inf.read().split('<Iteration>')[1:]]

        ## not so comprehensive list comprehensions wherein i parsed twice :))
        ## lwh = lenghts with hits, lwoh = length without hits
        lwh = [int(re.findall(r'<Iteration_query-len>(.*?)</Iteration_query-len>', line)[0]) \
                                for iteration in iterations if 'Hit_def' in iteration\
                                for line in iteration.split('\n') if '<Iteration_query-len>' in line]
        lwoh = [int(re.findall(r'<Iteration_query-len>(.*?)</Iteration_query-len>', line)[0]) \
                                for iteration in iterations if 'Hit_def' not in iteration\
                                for line in iteration.split('\n') if '<Iteration_query-len>' in line]


        ranges = [(100,500),(500,1000),(1000,1500),(1500,2000),(2000,2500), (2500,3000), (3000)]

        total = count_ranges(ranges, lwh) + count_ranges(ranges, lwoh)

        check(iterations, total)


def main():
    summ_evalue(blastxml)
    summ_tax(blastxml)
    summ_hits_by_len(blastxml)

if __name__ == '__main__':
    main()