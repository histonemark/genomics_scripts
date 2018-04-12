import sys
from gzopen import gzopen

# Parse

with gzopen(sys.argv[1]) as f:
   for line in f:
      if line[:2] != 'FB': continue
      nl = line.split()
      write = 'chr%s\t%d\t%d\t%s\t%s\n' %(nl[1], int(nl[3]), int(nl[3])+1, (nl[2]),(nl[0]))
      sys.stdout.write(write)
