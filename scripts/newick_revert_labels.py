#!/usr/bin/env python3.6

# -*- coding: utf-8 -*-
# @Author: Marylette Roa
# @Date:   2017-09-24 22:35:54
# @Last Modified by:   marylette
# @Last Modified time: 2017-10-30 15:32:48

from sys import argv, exit

def create_dictionary_from_map(header_file):
    with open(header_file) as inf:
        headers = {line.strip().split('\t')[1]:line.split('\t')[0] for line in inf.readlines()}
    return(headers)

def change_tree(tree_file, headers):
    with open(tree_file) as inf:
        tree = inf.read()
        for header in headers:
            tree = tree.replace(header,headers[header])
    return(tree)


def print_tree(tree):
    prefix = '.'.join(tree_file.split('.')[:-2])
    outfname = f'{prefix}.reverted_tree.txt'
    outf = open(outfname,'w')
    print(tree, file=outf)
    print(f'Output: {outfname}')
    outf.close()

def main():
    headers = create_dictionary_from_map(header_file)
    tree = change_tree(tree_file, headers)
    print_tree(tree)

if __name__ == '__main__':
    try:
        tree_file = argv[1]
        header_file = argv[2]
    except IndexError:
        help = f'''Usage: {argv[0]} <newick_file> <maps.txt>
       maps.txt: <true_label><tab><newick_label>'''
        print(help)
        exit()

    main()