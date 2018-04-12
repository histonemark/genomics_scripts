import sys
import pdb
#pdb.set_trace()
with open(sys.argv[1]) as f:
   for line in f:
      try:
         items = line.split()
         coord = items[-1].split(',')
         if len(coord) >1 : continue
         out =  coord[-1].split(':')
         sys.stdout.write('chr%s\t%s\n' % (out[0],out[2]))
      except:
         sys.stderr.write(line)