from sys import argv, exit

def get_header_desc(headers):
    with open(headers) as inf:
        descriptions = {desc.split(' ')[0].split('>')[1]: ' '.join(desc.split(' ')[1:]).rstrip() for desc in inf.readlines()}
        return(descriptions)

def acc2desc(headers,blast):
    outfile = f'{blast}.labeled'
    outf = open(outfile,'w')
    descs = get_header_desc(headers)
    with open(blast) as inf:
        labeled = [f'{line.strip()}\t{descs[line.strip().split()[1]]}' for line in inf.readlines()]
        print('\n'.join(labeled),file=outf)
        print(f'Output: {outfile}')

def main():
    if len(argv) != 3:
        about = 'Adds header labels to blast tsv output'
        usage = f'Usage: {argv[0]} <headers.txt> <blast.tsv>'
        print(f'{about}\n{usage}')
        exit()
    else:
        headers = argv[1]
        blast = argv[2]
        acc2desc(headers,blast)

if __name__ == '__main__':
    main()
