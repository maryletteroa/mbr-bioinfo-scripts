import urllib

from lxml import html, etree
from time import sleep
import sys

def retrieve_tbvar_results(pos):
    surl = "http://genome.igib.res.in/cgi-bin/tbvar/tbvar.cgi?query={}&hidden=variation".format(pos)
    page = html.fromstring(urllib.urlopen(surl).read())
    ltd = []
    for td in page.xpath("//td"):
        if td.text == None: pass
        else: ltd.append(td.text)
    la = []
    for a in page.xpath("//a"):
        if a.text == None: pass
        else: la.append(a.text)

    return(ltd,la)



h37rv_pos = range(1,4411533,1)
#print(h37rv_pos[-1], h37rv_pos[0])
#h37rv_pos = ['1095672', '3376995', '333680', '2163790', '1637192', '761139', '4247431', '2155168', '1473246', '761155']

known = open("in_tb_var.txt","w")
unknown = open("not_in_tb_var.txt","w")

for pos in  h37rv_pos:
	td, ta = retrieve_tbvar_results(pos)
	msg = "{} {} {}\n".format(pos, td,ta)
	if td == [] and ta == []: unknown.write(msg)
	else: known.write(msg)
	counter = "searching position {}/{} ... \r".format(pos,h37rv_pos[-1])
	print(counter),
	sys.stdout.flush()
	#sleep(0.5)
unknown.close()
known.close()







	

