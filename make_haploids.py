import sys
import pdb
from collections import defaultdict

maskdict = defaultdict(list)
chromn = ''

# Construct the dictionary of SNPs
with open(sys.argv[1],'r') as f:
   for line in f:
      items = line.split()
      chrom = items[0]
      # 0 based coordinate
      posit = int(items[1]) - 1
      snp1  = items[2] 
      snp2  = items[3]
      mask = len(snp1) if len(snp1) > len(snp2) else len(snp2)
      # An entry of the dict: chrX [1109,3]
      maskdict[chrom].append([posit,mask])
   
      
with open(sys.argv[2],'r') as g:
   for line in g:
      if line[0] == '>':
         chromn = line.split('>')[1].rstrip()
         sys.stdout.write('>%s\n' % chromn)
         if chromn == 'chr10':
           pdb.set_trace()
      else:
         dna = line.rstrip()
         for snpos in maskdict[chromn]:
            tomask = 'N' * int(snpos[1])
            dna = dna[:snpos[0]] + tomask + dna[snpos[0] + len(tomask):]
                  
         for i in xrange(0,len(dna),80):
            sys.stdout.write('%s\n' % dna[i:i+80])
         