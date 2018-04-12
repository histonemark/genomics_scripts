import sys

with open(sys.argv[1]) as f:
   for line in f:
      items = line.split()
      if items[7] != 'gene': continue
      out = (items[0],items[1],items[2],items[5],items[3])
      sys.stdout.write('%s\t%s\t%s\t%s\t%s\n' % out)