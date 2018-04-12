import sys
import re
import seeq
import pdb
import os
#from automata import PatternMatcher
from itertools import izip
from gzopen import gzopen

#pdb.set_trace()
fname1 = sys.argv[1]
fname2 = sys.argv[2]

#hind = seeq.compile('AAGCTAGCTT', 1)
dpn  = seeq.compile('GATC', 0)
# Open 2 files to write
out1 = re.sub(r'.fastq(\.gz)?', 'read1.fasta',os.path.basename(fname1))
out2 = re.sub(r'.fastq(\.gz)?', 'read2.fasta',os.path.basename(fname2))

# We cut in enzyme restriction site GATC (DpnII) and make a fasta file
# Or cut in                         AAGCTAGCTT (HindIII)  
with gzopen(fname1) as f, gzopen(fname2) as g, \
     open(out1,'w') as y, open(out2,'w') as z:
   for lineno,(line1,line2) in enumerate(izip(f,g)):
      if lineno % 4 != 1: continue

      seq1 = dpn.matchPrefix(line1, False) or line1.rstrip()
      seq2 = dpn.matchPrefix(line2, False) or line2.rstrip()
      if len(seq1) > 16 and len(seq2) > 16:
         y.write('>%d\n' % (lineno / 4))
         y.write(seq1 + '\n')
         z.write('>%d\n' % (lineno / 4))
         z.write(seq2 + '\n')
