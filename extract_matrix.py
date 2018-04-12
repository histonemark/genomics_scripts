#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import sys
import pdb
size = 1352000
resolution = 2000
N = size / resolution
 
out = [[0]*N for i in range(N)]
#pdb.set_trace()
with open(sys.argv[1]) as f:
   for line in f:
      try:
         A,B = re.sub(r'\t.*', '', line).split(';')
         chrA,locA = A.split(':')
         chrB,locB = B.split(':')
         if chrA != '4' or chrB != '4': continue
         locA = int(locA) / 50000
         locB = int(locB) / 50000
         if locA < N and locB < N:
            out[locA][locB] += 1
            out[locB][locA] += 1
      except Exception:
         sys.stderr.write(line)
      
for i in range(N):
   print '\t'.join([str(a) for a in out[i]])

# Zoom in a region Xbp

# start,end = 2000000,4000000
# res = 500
# N = (end - start) / res 
# out = [[0]*N for i in range(N)]
# #pdb.set_trace()
# with open(sys.argv[1]) as f:
#    try:
#       for line in f:
#          A,B = re.sub(r'\t.*', '', line).split(';')
#          chrA,locA = A.split(':')
#          chrB,locB = B.split(':')
#          if chrA != '2L' or chrB != '2L': continue
#          if not start < int(locA) < end: continue
#          if not start < int(locB) < end: continue
#          locA = (int(locA) - 2000000) / res
#          locB = (int(locB) - 2000000) / res
#          out[locA][locB] += 1
#          out[locB][locA] += 1
#    except Exception:
#       sys.stderr.write(line)

# for i in range(N):
#    print '\t'.join([str(a) for a in out[i]])