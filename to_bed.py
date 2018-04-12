import sys
import pdb

#pdb.set_trace()
with open(sys.argv[1]) as f:
   for line in f:
      items = line.split()
      sys.stdout.write('chr%s\t%s\t%s\t%s\n' % (items[1],items[3],items[3],items[9]))