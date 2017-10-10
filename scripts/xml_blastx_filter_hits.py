#!/usr/bin/python
'''
@MaryletteRoa
17-May-2017
'''
from sys import argv, path, exit
# path.append('/mnt/e/virtual_envs/windowsEnv/lib/python3.4/site-packages')
# from Bio.Blast import NCBIXML
import xml.etree.ElementTree as ElementTree
from datetime import datetime

def getFirstHits(xml):
    '''filters the blastx xml for first hits only, outputs an xml file'''
    print('getting first hits')
    with open(xml) as f:
        tree = ElementTree.parse(f)
        root = tree.getroot()
    hit_count = 0 # counts the first hits only
    for hit in root.iter('Hit'):
        for hitnum in hit.iter('Hit_num'):
            if int(hitnum.text) > 1:
                # print(hitnum.tag, hitnum.text)
                hit.clear()
            else:
                hit_count += 1
    print('number of hits', hit_count)
    time = str(datetime.now()).split('.')[0].replace('-','_').replace(':','_').replace(' ','_')
    outf = 'filt_{}_{}.xml'.format(xml.replace('.','_'), time)
    tree.write(outf)
    print('Output:', outf)
    return(tree)

# ## under construction ###
# def getLowFrequencyHits(tree):
#     print('getting low frequencing hits')
#     ids = []
#     low_frequency_ids = []
#     root = tree.getroot()
#     for id in root.iter('Hit_id'):
#         ids.append(id.text)
#     for id in set(ids):
#         if ids.count(id) < 5:
#             low_frequency_ids.append(id)
#     print('number of low frequency hits', len(low_frequency_ids))
#     # print(low_frequency_ids)
#     return(low_frequency_ids)

# def removeIds(tree, ids):
#     root = tree.getroot()
#     for hit in root.iter('Hit'):
#         for id in root.iter('Hit_id'):
#             if id.text in ids:
#                 hit.clear()
#     return(tree)
# ## under construction ###

if __name__ == '__main__':
    try:
        xml = argv[1]
    except IndexError:
        help = ''''foo.py <file.xml>'''
        print(help)
        exit()

    tree = getFirstHits(xml)
    # ids = getLowFrequencyHits(tree)
    # removeIds(tree, ids)