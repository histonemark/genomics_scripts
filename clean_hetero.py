#!/usr/bin/env python

import sys

allowed = ['chr2R','chr2L','chr3R','chr3L','chr4','chrX']
with open(sys.argv[1]) as f:
   for line in f:
      if not line.split()[0] in allowed: pass
      else: sys.stdout.write(line)
