# -*- coding:utf-8 -*-

# This script takes 5'UTR regions of every Drosophila annotated gene in flybase to associate it with experimental modENCODE TSS's from 5' Race experiments

import re
import sys

from gzopen import gzopen


records = {}

# First we create the header of the file
sys.stdout.write('FBgnID\tchromosome\tstrand\tstartUTR\tendUTR\n')

# Open the Fasta file from Flybase with all the annotated 5'UTR's 
with gzopen('dmel-all-five_prime_UTR-r5.52.fasta.gz') as f:
   for line in f:
      # We work with the Fasta header of each entry:
      # >FBtr0086024 type=five_prime_untranslated_region; loc=2R:complement(1946941..1947063); 
      # name=CG7856-RA; MD5=0e29152561825b6636f4f7408d1ccfbb; length=123; parent=FBgn0033056; release=r5.52; species=Dmel;  
      if line[0] != '>': continue
      (chrom, ori, start, end, parent) = re.search(
            r'loc=([^:]+):(join\(|complement\()?(\d+)\.[\d.,]*\.(\d+).*parent=(FBgn\d{7})',
            line).groups()
      strand = '-' if ori == 'complement(' else '+'
      # Keep only the shortest 5'UTR for a given start position.
      realstart = start if strand == '+' else end
      if records.has_key((parent, realstart)):
         record = records[(parent, realstart)]
         if int(end) - int(start) > int(record[4]) - int(record[3]):
            continue
      records[(parent, realstart)] = (parent, chrom, strand, start, end)

for key,record in sorted(records.items()):
   sys.stdout.write('%s\t%s\t%s\t%s\t%s\n' % record)
