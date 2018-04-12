import sys
import pdb
from itertools import izip

with open(sys.argv[1]) as f,open(sys.argv[2]) as g:
   for (line1,line2) in izip(f,g):
      if line1[:3] != 'SRR': continue
      
      items1 = line1.split()
      items2 = line2.split()
      # Trash the line if fwd or rev non mapped.
      if items1[2] == '*' or items2[2] == '*': continue
      # If none of the reads map with different quality trash.
      #pdb.set_trace()
      AS1 = int(items1[13].split(':')[-1])
      XS1 = int(items1[14].split(':')[-1])
      if AS1 != XS1:
         fwd = 'ok'
      else:
         fwd = 'no'

      AS2 = int(items1[13].split(':')[-1])
      XS2 = int(items1[14].split(':')[-1])
      if AS2 != XS2:
         rev = 'ok'
      else:
         rev = 'no'

      if fwd == 'ok' and \
         rev == 'ok':
         sys.stdout.write('%s;%s\n' % (items1[2],items2[2]))
      elif fwd == 'ok' and \
           rev == 'no':
         inferred = items2[-1].split(',')[0][5:]
         sys.stdout.write('%s;%s\n' % (items1[2], inferred))
      elif fwd == 'no' and \
           rev == 'ok':
         inferred = items1[-1].split(',')[0][5:]
         sys.stdout.write('%s;%s\n' % (inferred2, items2[2]))
      else:
         continue # Cannot tell wich haplo they belong to.
                          
            