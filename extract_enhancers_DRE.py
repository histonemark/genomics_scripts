import sys
import os
import pickle
import re
import pdb

#pdb.set_trace()
# We load the genome index and print sequence.
GINDEX = pickle.load(open('/mnt/shared/bin/dm3R5.pck'))
KEEP   = ['2L','2R','3L','3R','X','4']


def fetch_as_fasta(chrom,start,end,gindex,fname):
   """Parses genome coordinates in one of two ways, extract the
   corresponding sequence from the index file and prints it with
   a fasta header."""
   
   # Print the sequence in fasta format.
   header = '>%s:%s-%s' % (chrom, start, end)
   fname.write('%s\n%s\n' % (header, gindex[chrom][start:end]))


# We open the file with all the genes per color in Kc167 cells and we extract
# the coordinates of all the genes per color
   
with open(sys.argv[1]) as f:
   activ = open('DRE_activators.txt','w')
   inhib = open('DRE_inhibitors.txt','w')
   for line in f:
      items = line.split()
      chrom = re.sub(r'^chr', '', items[0])
      center = items[1]
      start =  int(center) - 50
      end   =  int(center) + 50
      value = float(items[2])

      if value > 2.1 and chrom in KEEP:
         fetch_as_fasta(chrom,start,end,GINDEX,activ)
      elif value < 2.1 and chrom in KEEP:
         fetch_as_fasta(chrom,start,end,GINDEX,inhib)
      else:
         continue
         