# -*- coding: utf-8 -*-
# @Author: marylette
# @Date:   2017-11-04 09:59:12
# @Last Modified by:   marylette
# @Last Modified time: 2018-07-18 10:34:38


from sys import argv, exit

def read_fastas(fasta_file):
    with open(fasta_file) as inf:
        sequences = [line for line in inf.read().split('>')[1:]]
        fastas = {sequence.split('\n')[0]:''.join(sequence.strip().split('\n')[1:]) for sequence in sequences}
        return(fastas)

def rewrite_fastas(fastas,delimiter):
    prefix = '.'.join(fasta_file.split('.')[0:-1])
    outf_name = f'{prefix}.shortname.fasta'
    outf = open(outf_name, 'w')
    for fasta in fastas:
        header = fasta.split(delimiter)[0]
        sequence = fastas[fasta]
        fasta_p = f'>{header}\n{sequence}'
        print(fasta_p, file=outf, end='\n')
    print(f'Output: {outf_name}')
    outf.close()





def main():
    fastas = read_fastas(fasta_file)
    rewrite_fastas(fastas, delimiter)


if __name__ == '__main__':
    try:
        fasta_file = argv[1]
        delimiter = argv[2]
    except IndexError:
        help = f'{argv[0]} <sequence.fasta> <delimiter>'
        print(help)
        exit()

    main()