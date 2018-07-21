# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2018-03-08 20:16:26
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2018-07-18 10:38:43

import sys
sys.path.append('/mnt/e/virtual_envs/windowsEnv/lib/python3.4/site-packages')
import xlrd, csv, os, datetime


def convertXlsxToTsv(workbook):
    outdir = '_'.join(workbook.split('.')).replace(' ','_')
    # create an output directory
    # if exists, do not create
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    else:
        pass
    xls = xlrd.open_workbook(xlsname)
    print('Reading file {}'.format(xlsname))
    sheetnames = xls.sheet_names()
    numsheets = xls.nsheets
    writenum = 0
    for n in range(0,numsheets):
        print('Reading sheet {}'.format(sheetnames[n]))
        sheet = xls.sheet_by_name(sheetnames[n])
        tsvname = '{}.tsv'.format(sheetnames[n].replace(' ','_'))
        outpath = os.path.join(outdir,tsvname)
        # if a tsv exists, do nothing
        # hence, erase existing tsvs of the same name as outputs
        # to generate new tsvs .. this is to avoid overwriting
        # the previous tsv
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
                # Important! make sure that the dates in the excel are in the Date format, if in Text format, the script will return the value as is
                # # could be broken down to more variables
                    # date = datetime.datetime.strptime(str(datetime.datetime(1899, 12, 30) + datetime.timedelta(int(sheet.cell_value(row,col))))[:10], '%Y-%m-%d').strftime('%m/%d/%Y')
                    reference_date = datetime.datetime(1899, 12, 30)
                    converted_date = datetime.timedelta(int(sheet.cell_value(row,col)))
                    date = datetime.datetime.strptime(str(reference_date + converted_date)[:10], '%Y-%m-%d').strftime('%m/%d/%Y')

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
        print('  Hidden cells and sheets are also printed out')
        sys.exit()

    try: 
        convertXlsxToTsv(xlsname)
    except FileNotFoundError:
        print('Error: Make sure {} exists!'.format(xlsname))
        exit()