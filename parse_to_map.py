#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pdb
import seeq
import sys
from gzopen import gzopen
from itertools import izip

pT2 = seeq.compile('TGTATGTAAACTTCCGACTTCAACTGTA', 5)
MIN_BRCD = 15
MAX_BRCD = 25
MIN_GENOME = 15

#pdb.set_trace()
outfname = sys.argv[1].split("_")[0] +  ".tomap"

with gzopen(sys.argv[1]) as f, gzopen(sys.argv[2]) as g, \
      open(outfname, 'w') as outf:
      # Aggregate iterator of f,g iterators -> izip(f,g).
      for lineno,(line1,line2) in enumerate(izip(f,g)):
         # Take sequence only.
         if lineno % 4 != 1: continue
         # Split on "CATG" and take the first fragment.
         # In case there is no "CATG", the barcode will be rejected
         # for being too long.
         brcd = line1.rstrip().split('CATG')[0]
         if not MIN_BRCD < len(brcd) < MAX_BRCD: continue
         # Use a Levenshtein automaton to find the transpsoson.
         genome = pT2.trimPrefix(line2, False)
         if not genome: continue
         # Select the region from the end of the transposon to
         # the first "CATG", if any.
         genome = genome.split('CATG')[0].rstrip()
         if len(genome) < MIN_GENOME: continue
         outf.write('>%s\n%s\n' % (brcd,genome))
