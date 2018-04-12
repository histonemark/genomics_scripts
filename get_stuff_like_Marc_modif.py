#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import sys

from collections import defaultdict

keep = ('2L', '2R', '3L', '3R', '4', 'X','pT2')

def histo():
   return defaultdict(int)

def dist(intlist):
   intlist.sort()
   try:
      if intlist[0][0] != intlist[-1][0]: return float('inf')
      return intlist[-1][1] - intlist[0][1]
   except IndexError:
      return float('inf')

canonical = dict()
with open(sys.argv[1]) as f:
   for line in f:
      items = line.split()
      for brcd in items[2].split(','):
         canonical[brcd] = items[0]

counts = defaultdict(histo)
with open(sys.argv[2]) as f:
   for line in f:
      items = line.split()
      try:
         barcode = canonical[re.sub(r':[^:]+$', '', items[0])]
      except KeyError:
         continue
      if items[3] == '-':
         position = ('', 0)
      else:
         pos = items[3].split(':')
         position = (pos[0], int(pos[2]))
         counts[barcode][position] += 1


integrations = dict()
for brcd,hist in counts.items():
   total = sum(hist.values())
   top = [pos for pos,count in hist.items() if count > max(1, 0.1*total)]
   if dist(top) > 10: continue
   ins = max(hist, key=hist.get)
   integrations[brcd] = ins

for brcd in sorted(integrations, key=integrations.get):
   chrom,pos = integrations[brcd]
   if chrom not in keep: continue
   sys.stdout.write('%s\t%s\t%d\n' % (brcd,chrom,pos))
