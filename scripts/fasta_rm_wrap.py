# -*- coding: utf-8 -*-
# @Author: Marylette Roa
# @Date:   2017-11-09 15:49:52
# @Last Modified by:   marylette
# @Last Modified time: 2018-07-18 10:34:33

from sys import argv, exit

def read_fasta(fasta_file):
    with open(fasta_file) as inf:
        fastas = {line.split('\n')[0].strip('>').strip():''.join(line.strip().split('\n')[1:]) for line in inf.read().split('>')[1:]}
        return(fastas)

def write_fasta(fasta_file, fastas):
    prefix = fasta_file.split('.')[0]
    outf_name = f'{prefix}.unwrapped.fasta'
    outf = open(f'{outf_name}','w')
    for fasta in fastas:
        sequence = f'{fastas[fasta]}'
        fasta_p = f'>{fasta}\n{sequence}'
        print(fasta_p, file=outf, end='\n')
    print(f'Output: {outf_name}')
    outf.close()


def main():
    fastas = read_fasta(fasta_file)
    write_fasta(fasta_file, fastas)
    


if __name__ == '__main__':
    try: 
        fasta_file = argv[1]
    except IndexError:
        help = './fasta_rm_wrap.py <seq.fasta>'
        print(help)
        desc = 'removes multiline in fasta file'
        print(desc)
        exit()
    main()