#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import sys

wsz = 2000

chroms = {
      '2L': 23011546,
      '2R': 21146710,
      '3L': 24543559,
      '3R': 27905055,
      '4':  1351859,
      'X':  22422829,
}

diag = dict()
subdiag = dict()
therest = dict()
for (chrom,size) in chroms.items():
   diag[chrom] = [0]*(1+ size/wsz)
   subdiag[chrom] = [0]*(1+ size/wsz)
   therest[chrom] = [0]*(1+ size/wsz)

with open(sys.argv[1]) as f:
   for line in f:
      try:
         A,B = re.sub(r'\t.*', '', line).split(';')
      except ValueError:
         sys.stderr.write(line)
         continue
      chrA,locA = A.split(':')
      chrB,locB = B.split(':')
      if chrA not in chroms or chrB not in chroms: continue
      locA = int(locA) / wsz
      locB = int(locB) / wsz
      if chrA == chrB:
         if locA == locB:
            diag[chrA][locA] += 2
            continue
         if abs(locA-locB) < 3:
            subdiag[chrA][locA] += 1
            subdiag[chrB][locB] += 1
            continue
      therest[chrA][locA] += 1
      therest[chrB][locB] += 1

for chrom in chroms:
   D = diag[chrom]
   S = subdiag[chrom]
   R = therest[chrom]
   for i in range(len(S)):
      print "%s\t%d\t%d\t%d" % (chrom, D[i], S[i], R[i])
