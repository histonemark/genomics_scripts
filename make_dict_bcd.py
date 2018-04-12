import sys
import os
from collections import defaultdict
#import pdb;pdb.set_trace()

def histo():
    return defaultdict(int)

bcd_dict = {}
# File after starcoding -> canonical count degenerates (CSL)
# Name pX_RZ_.txt_map_clust
with open(sys.argv[1]) as f:
    for line in f:
        items = line.split()
        canonical = str(items[0])
        derivates = items[2].split(',') # CSV list of barcodes 
        # Construc a dictyonary Key:value -> degenerate:canonical
        for derivate in derivates:
            bcd_dict[derivate] = canonical

# This file must be the mapped version wich contains all the barcodes. The name is in the form of pX_RX.txt.map.             
ins_dict = defaultdict(histo)
with open(sys.argv[2]) as f:
    for line in f:
        items = line.split()
        barcode = items[0].split(':')[0]
        try:
            position = items[-1].split(':')[0] + ' ' + items[-1].split(':')[2]
        except IndexError:
            continue
        try:
            canonical = bcd_dict[barcode]
        except KeyError:
            continue
        #for key,value in sorted(bcd_dict.iteritems()):
        #    if barcode == key:
        ins_dict[canonical][position] += 1
        #ys.stdout.write('%s\t%s\n' % (canonical,position))

for canonical,histo in sorted(ins_dict.items()):
    barcode  = canonical
    tmp_list = []
    for insertion,count in histo.items():
        if not count > 1: continue 
        chromosome = insertion.split()[0] 
        position   = insertion.split()[1]
        tmp_list.append([chromosome,position,count])
    if not len(tmp_list) > 0: continue
    for position in tmp_list:
        
        
    sys.stdout.write('%s\t\n' % (barcode))
    sys.stdout.write('  %s\n' % (tmp_list))
        
