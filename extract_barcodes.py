import sys
import os 

with open(sys.argv[1]) as f:
    wd = os.getcwd()
    name = os.path.join(wd,sys.argv[1])
    out = open( name + '_barcodes','w')
    non_mapped = 0
    pt2_mapped = 0
    for line in f:
        items = line.split()
        if items[-1] == '-': continue
        barcode    = items[0].split(':')[0]
        #chromosome = items[-1].split(':')[0]
        #location   = items[-1].split(':')[2]
        out.write('%s\n' % (barcode))
        
