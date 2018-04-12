import sys 
from collections import defaultdict

integrations = defaultdict(lambda: defaultdict(int))
with open(sys.argv[1]) as f:
   for line in f:
      items = line.split()
      barcode = items[0]
      pos     = '_'.join([items[1],items[2],items[3]]) 
      integrations[barcode][pos] += 1
   
for key in integrations:
   lugares = integrations[key]
   for lugar in lugares:
      (chrom,strand,pos) = lugar.split('_')
      count = integrations[key][lugar]
      toprint = (key,chrom,strand,pos,count)
      sys.stdout.write('%s\t%s\t%s\t%s\t%s\n' % toprint)         
      
