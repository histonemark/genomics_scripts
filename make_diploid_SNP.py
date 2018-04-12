import sys
import pdb
from collections import defaultdict

SNPDICT = defaultdict(list)


# We first construct a dictionary with the [chr] {posit,SNPa,SNPb}
with open(sys.argv[1]) as f:
   for line in f:
      items = line.split()
      chrom = items[0]
      posit = items[1] # Is a bed file so it's already 0 based
      snpA  = items[2]
      snpB  = items[3]
      SNPDICT[chrom].append([posit,snpA,snpB])

# We read the haploid ref genome with one chr per line
# we transform into a list and change the SNPs from dict

hapA = open('mm9_HapA.fasta','w')
hapB = open('mm9_HapB.fasta','w')
#pdb.set_trace()      
with open(sys.argv[2]) as g:
   for line in g:
      if line[0] == '>':
         chrname = line.rstrip()[1:]
      else:
         seq2a = list(line.rstrip())
         seq2b = list(line.rstrip())

         # We introduce the SNPS into list positions (doesnt change base position)
         for snpos in SNPDICT[chrname]:
            seq2a[int(snpos[0])] = snpos[1]
            seq2b[int(snpos[0])] = snpos[2]

         # We print the 2 haplotype genomes
         for i in xrange(0,len(seq2a) +1 ,1000):
            hapA.write('>%s:%s-%s_A\n' % (chrname,i,i+1000))
            hapA.write(''.join(seq2a[i:i+1000]) + '\n')
            hapB.write('>%s:%s-%s_B\n' % (chrname,i,i+1000))
            hapB.write(''.join(seq2b[i:i+1000]) + '\n')