import sys
import pdb
from collections import defaultdict


snpdict = defaultdict(list)
chrname = ''
# Construct the dictionary of SNPs
with open(sys.argv[1],'r') as f:
   for line in f:
      items = line.split()
      chrom = items[0]
      posit = int(items[1])
      snp1  = items[2]
      snp2  = items[3]
      # An entry of the dict: chr: [1109,A,AAT]
      snpdict[chrom].append([posit,snp1,snp2])
#set_trace()
# Read the index genome and create 2 haplotype sequences from dictionary entries
with open(sys.argv[2],'r') as g:
   for seq in g:
      if seq[0] == '>':
         chrname = seq.split('>')[1].rstrip()
      else:
          chrlen = len(seq)
          for snpos in snpdict[chrname]:
              pos  = snpos[0] - 1   # we want the position in 0-base
              snpA = snpos[1]
              snpB = snpos[2]
   
              lineA = seq[max(0,pos - 74):pos] + snpA + seq[pos+1:pos  + 75]
              lineB = seq[max(0,pos - 74):pos] + snpB + seq[pos+1:pos  + 75]

              # Print line A.
              sys.stdout.write('>'+chrname+"_"+ str(pos) +'_A\n')
              sys.stdout.write(lineA+'\n')
              # Print line B.
              sys.stdout.write('>'+chrname+"_"+str(pos)+'_B\n')
              sys.stdout.write(lineB+'\n') 


