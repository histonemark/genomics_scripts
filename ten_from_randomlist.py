
# Imports
import sys
from gzopen import gzopen
import pdb

# Take 10 sequences
#pdb.set_trace()
counter = 0
with gzopen(sys.argv[1]) as f:
   for line in f:
      if line[0] == '>':
         counter = counter + 1
      if counter > 10: break
      sys.stdout.write(line)
