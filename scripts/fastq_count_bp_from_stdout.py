# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:35:33

'''
counts bp from stream
'''
import fileinput

def checkseq(line):
        dna = "ACTG"
        counter = 0
        for char in line:
                if char not in dna: counter = counter + 1
        if counter == 0: return line

total_count = 0
for line in fileinput.input():
        if line.startswith("@") | line.startswith("+") == False:
                seq = checkseq(line.strip())
                if seq != None: total_count = total_count + len(seq)
print( total_count)