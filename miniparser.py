# -*- coding:utf-8 -*-

# Invoked like so:
# `python miniparser.py dmel-all-gene-r5.50.fasta.gz | sort -k2,2 -k4,4n | gzip > annotated_TSS_r.50.txt.gz`

import sys
import re
from gzopen import gzopen

with gzopen(sys.argv[1]) as f:
   for line in f:
      if line[0] != '>': continue
      #>FBgn0033056 type=gene; loc=2R:complement(1944862..1947063);
      items = re.match(r'>(FBgn\d{7}).*?loc=([^:]+):(complement\()?' \
         '(\d+)\.\.(\d+)', line).groups()
      strand = '+' if items[2] is None else '-'
      TSS = items[3] if strand == '+' else items[4]
      sys.stdout.write('%s\t%s\t%s\t%s\n' % \
            (items[0], items[1], strand, TSS))
