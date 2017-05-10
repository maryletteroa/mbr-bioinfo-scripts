'''
@MaryletteRoa
10-May-2017
'''

import sys
sys.path.append('/mnt/e/virtual_envs/windowsEnv/lib/python3.4/site-packages')
import xlrd, csv, os, datetime


def convertXlsxToTsv(workbook):
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
        tsv = open(outpath,'w')
        writenum += 1
        print('Writing into file {}'.format(outpath))
        wout = csv.writer(tsv, delimiter = '\t')
        for row in range(0,sheet.nrows):
            wrow = []
            for col in range(0, sheet.ncols):
                if sheet.cell(row,col).ctype == xlrd.XL_CELL_DATE:
                    date = datetime.datetime.strptime(str(datetime.datetime(1899, 12, 30) + datetime.timedelta(int(sheet.cell_value(row,col))))[:10], '%Y-%m-%d').strftime('%d/%m/%Y')
                    wrow.append(date)
                else:
                    wrow.append(str(sheet.cell_value(row,col)))
            srow = '\t'.join(wrow)
            tsv.write(srow +'\n')
    tsv.close()
    print('Total number of sheets found {}'.format(numsheets))
    print('Total number of sheets converted {}'.format(writenum))
    print('Done')

if __name__ == '__main__' :

    try:
        xlsname = sys.argv[1]
    except IndexError:
        print('Usage: foo.py <file.xlsx>')
        print(' Converts an *.xlsx file to *.tsv files per sheet')
        sys.exit()

    outdir = '_'.join(xlsname.split('.')).replace(' ','_')
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    else:
        pass

    convertXlsxToTsv(xlsname)
