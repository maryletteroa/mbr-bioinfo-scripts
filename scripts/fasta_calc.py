from sys import argv, exit

try:
    fasta = argv[1]
except IndexError:
    about = '''Outputs %GC per contig. Calculates only over ATGC characters. 
    Non-ATGC are not counted in the overall length of the sequence.
    Python3.6.x syntax.'''
    usage = '\nfoo.py <seq.fasta>'
    print(about)
    print(usage)
    exit()

with open(fasta) as inf:
    for line in inf.readlines():
        if line.startswith('>'):
            header = line.strip().split('>')[1]
        else:
            seq = line.strip().upper()
            at = seq.count('A') + seq.count('T')
            gc = seq.count('G') + seq.count('C')
            length = gc + at
            prec_gc = round((gc / length) * 100.0,2)
            print(f'{header}\t{prec_gc}')
