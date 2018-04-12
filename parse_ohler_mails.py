import sys
import os


MAILIST = os.listdir('.')

for element in MAILIST:
   inf = open(element,'r')
   MAILIST.remove(element) 
   for line in inf:
      if line[0] == '>':
         sys.stdout.write('%s\n' % line)