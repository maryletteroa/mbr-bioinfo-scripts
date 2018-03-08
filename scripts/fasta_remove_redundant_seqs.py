from sys import argv,exit


try:
    fasta_file  = argv[1]
except IndexError:
    about = '''
Remove redundant fasta sequences (completely identical characters) from a multi-fasta file
'''
    usage = f'  Usage: {argv[0].split("/")[-1]} <sequence.fasta>'
    print(about, usage)
    exit()



with open(fasta_file) as inf:
    seqs = inf.read().split('>')[1:]

nrseqs = list(set(seqs))

nrseqs_out = ('>'+'>'.join(nrseqs))

outname = f'{fasta_file}.nrseqs.fasta'
fout = open(outname, 'w')
fout.write(nrseqs_out)
fout.close()

print(f'Output: {outname}')



