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
    bk = open('black_proms.txt','w')
    bl = open('blue_proms.txt','w')
    gn = open('green_proms.txt','w')
    rd = open('red_proms.txt','w')
    yw = open('yellow_proms.txt','w')
    # Skip the header
    f.readline()
    for line in f:
       items    = line.split()
       chrom    = items[0]
       color    = items[5]
       if items[3] == '+': 
          start    = int(items[1]) - 1000
          end      = int(items[1])
       else:
          start = int(items[2])
          end   = int(items[2]) + 1000
       if color == 'BLACK':
          fetch_as_fasta(chrom,int(start),int(end), gindex,bk)
       elif color == 'BLUE':
          fetch_as_fasta(chrom,int(start),int(end), gindex,bl)
       elif color == 'GREEN':
          fetch_as_fasta(chrom,int(start),int(end), gindex,gn)
       elif color == 'RED':
          fetch_as_fasta(chrom,int(start),int(end), gindex,rd)
       else:
          fetch_as_fasta(chrom,int(start),int(end), gindex,yw)