import pdb
import sys
import seeq
from collections import defaultdict

COMMON = seeq.compile('CTAGTTGTGGTTTGTCCAAACTCATCGAGCTCGAGA',3)
PROMD = defaultdict(int)

with open(sys.argv[1]) as f:
    for lineno,line in enumerate(f):
        if lineno % 4 != 1: continue
        barcode = COMMON.matchPrefix(line, False)
        prom    = COMMON.matchSuffix(line.rstrip(), False)
        if prom:
            PROMD[prom] += 1

#pdb.set_trace()

for k in PROMD:
    count = PROMD[k]
    sys.stdout.write('%s\t%d\n' % (k,count))
    
