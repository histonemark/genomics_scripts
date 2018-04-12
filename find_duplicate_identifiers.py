import sys
from collections import defaultdict
import pdb





# remove duplicated promoters
ident = defaultdict(int)

with open(sys.argv[1]) as f:
   for line in f:
      if line[0] == '>':
         ident[line] = ident[line] + 1
   f.seek(0)
   for line in f:
      if line[0] == '>' and ident[line] < 2:
         print line
         print_next = 'ON'
      elif line[0] != '>' and print_next == 'ON':
         print line
         print_next = 'OFF'
      else:
         continue

