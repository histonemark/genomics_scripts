#! /usr/bin/env python
import sys

with open(sys.argv[1]) as f:
   for line in f:
      items  = line.split()
      start  = items[-2]
      end    = items[-1]
      chrm   = items[-3]
      feat   = items[6]
      bind   = -1 if 'depleted' in line else 1 
      out    = (chrm,start,end,feat,bind)
      sys.stdout.write('chr%s\t%s\t%s\t%s\t%s\n' % out)
