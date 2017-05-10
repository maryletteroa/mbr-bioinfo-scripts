'''
@MaryletteRoa
10-May-2017
'''

import sys
sys.path.append('/mnt/e/virtual_envs/windowsEnv/lib/python3.4/site-packages')
import xlrd, csv, os
try:
    xlsname = sys.argv[1]
except IndexError:
    print('Usage: foo.py <file.xls>')
    print(' Converts an *.xls file to *.tsv files per sheet')
    sys.exit()

outdir = '_'.join(xlsname.split('.')).replace(' ','_')
if not os.path.exists(outdir):
    os.makedirs(outdir)
else:
    pass

print('Reading file {}'.format(xlsname))
xls = xlrd.open_workbook(xlsname)
sheetnames = xls.sheet_names()
numsheets = xls.nsheets
writenum = 0
for n in range(0,numsheets):
    print('Reading sheet {}'.format(sheetnames[n]))
    sheet = xls.sheet_by_name(sheetnames[n])
    tsvname = '{}.tsv'.format(sheetnames[n].replace(' ','_'))
    outpath = os.path.join(outdir,tsvname)
    if os.path.exists(outpath):
        print('File exists. Nothing to do.')
        continue
    with open(outpath,'w') as tsv:
        writenum += 1
        print('Writing into file {}'.format(outpath))
        wout = csv.writer(tsv, delimiter = '\t')
        for row in range(0,sheet.nrows):
            wout.writerow(sheet.row_values(row))
print('Total number of sheets found {}'.format(numsheets))
print('Total number of sheets converted {}'.format(writenum))
print('Done')