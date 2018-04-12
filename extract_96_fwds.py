import sys
import pdb
from string import maketrans


# A 96 well plate
comp = maketrans('ACTG', 'TGAC')

primern = 1543
with open(sys.argv[1]) as f:
    for line in f:
        items = line.rstrip().split(',')
        if items[2][:20] != 'gcatggtgaattccatggat': continue
        seq = items[2][20:].translate(comp)[::-1]
        well = items[0]
        primern += 1
        out = (well,'GAT' + str(primern),seq)
        sys.stdout.write('%s,%s,%s\n' % out)
        
