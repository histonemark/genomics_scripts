import sys
import os
import pickle
import re
#import pdb

#pdb.set_trace()
# We load the genome index and print sequence.
gindex = pickle.load(open('/mnt/shared/bin/dm3R5.pck'))


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
    # Lets oepn some file to write the output
    proms = open('proms.txt','w')
   
    # Skip the header
    f.readline()
    for line in f:
       items    = line.split()
       chrom    = items[0]
       color    = items[5]
       if items[3] == '+': 
          start    = int(items[1]) - 500
          end      = int(items[1]) + 100
       else:
          start = int(items[2]) - 100
          end   = int(items[2]) + 500
       fetch_as_fasta(chrom,int(start),int(end), gindex,proms)
