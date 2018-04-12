import sys
from itertools import izip
from collections import defaultdict



paird = defaultdict(int) 

with open(sys.argv[1]) as f,open(sys.argv[2]) as g:
   for (line1,line2) in izip(f,g):
      items1 = line1.split()
      items2 = line2.split()
      if items1[-1] == '-' or items2[-1] == '-':
         paird['-'] += 1
         continue
      try:   
         chr1 = items1[-1].split(':')[0]
         pos1 = items1[-1].split(':')[2]
         chr2 = items2[-1].split(':')[0]
         pos2 = items2[-1].split(':')[2]
         pair = chr1 + ':' + pos1 + ';' + chr2 + ':' + pos2
         paird[pair] += 1
      except IndexError:
         sys.stderr.write('Error in this lines %s\n%s\n' % (line1,line2))
         continue
         
   for k in paird:
      npair = paird[k]
      sys.stdout.write('%s\t%s\n' % (k,npair))
