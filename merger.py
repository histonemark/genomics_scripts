import sys
import pdb

from itertools import izip

with open(sys.argv[1],'r') as f, open(sys.argv[2]) as g:
   counter = 0
   for (line1,line2) in izip(f,g):
      if counter == 0:
         sys.stdout.write(line1)
         counter += 1
         continue
      if counter == 1:
         sys.stdout.write(line1.rstrip() + 'N' + line2)
         counter += 1
         continue
      if counter == 2:
         sys.stdout.write(line1)
         counter += 1
         continue
      if counter == 3:
         sys.stdout.write(line1.rstrip() + 'B' + line2)
         counter = 0
         