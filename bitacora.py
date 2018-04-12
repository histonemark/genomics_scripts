#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import subprocess
import sys
from automata import PatternMatcher
from collections import defaultdict
from gzopen import gzopen
from itertools import izip
from math import sqrt
from vtrack import vheader
#import pdb; pdb.set_trace()


########  Mapping Pipeline ###############################################

def extract_reads_and_write_fasta_file(fname_iPCR_PE1, fname_iPCR_PE2):
   """Some info."""
   # Params.
   MIN_BRCD = 15
   MAX_BRCD = 25
   MIN_GENOME = 15

   # The known parts of the sequences are matched with a Levenshtein
   # automaton. On the reverse read, the end of the transposon
   # corresponds to a 34 bp sequence ending as shown below. We allow
   # up to 3 mismatches/indels. On the forward read, the only known
   # sequence is the CATG after the barcode, which is matched exactly.
   TRANSPOSON = PatternMatcher('TGTATGTAAACTTCCGACTTCAACTGTA', 3)

   # Open a file to write
   fname_fasta_tomap = re.sub(r'fastq(\.gz)?', 'fasta', fname_iPCR_PE1)
   # Substitution failed, append '.fasta' to avoid name collision.
   if fname_fasta_tomap == fname_iPCR_PE1:
      fname_fasta_tomap = fname_iPCR_PE1 + '.fasta'
    
   with gzopen(fname_iPCR_PE1) as f, gzopen(fname_iPCR_PE2) as g, \
      open(fname_fasta_tomap, 'w') as outf:
      # Aggregate iterator of f,g iterators -> izip(f,g).
      for lineno,(line1,line2) in enumerate(izip(f,g)):
         # Take only sequence in line 2
         if lineno % 4 == 1:
         # Split on "CATG" and take the first fragment.
         # In case there is no "CATG", the barcode will be rejected
         # for being too long.
            brcd = line1.rstrip().split('CATG')[0]
            if not MIN_BRCD < len(brcd) < MAX_BRCD: continue
            # Use a Levenshtein automaton to find the transpsoson
            # sequence. Genomic position starts next position (equal
            # to 0 in case there is no match).
            gpos = TRANSPOSON.end(line2) + 1
            if gpos < 0: continue
            # Select the region from the end of the transposon to
            # the first "CATG", if any.
            genome = line2[gpos:].split('CATG')[0].rstrip()
            if len(genome) < MIN_GENOME: continue
            outf.write('>%s\n%s\n' % (brcd,genome))
   return fname_fasta_tomap


def call_gem_mapper(fname_fasta_tomap):
    """Some info."""
    INDEX   = '/mnt/shared/seq/gem/dm3R5/dm3R5_pT2_unmasked.gem'
    # Version info for `gem-mapper`.
    subprocess.call([
       'gem-mapper',
       '-I', INDEX ,
       '-i', fname_fasta_tomap,
       '-o', fname_fasta_tomap,
       '-m3',
       '-T4',
       '--unique-mapping',
    ])
    # Added by `gem`.
    return fname_fasta_tomap + '.map'
    

def call_starcode(fname_gem_mapped):
   """Some info."""
   fname_starcode_out = re.sub(r'\.gem$', '_starcode.txt', fname_gem_mapped)
   # Substitution failed, append '_starcode.txt' to avoid name collision.
   if fname_gem_mapped == fname_starcode_out:
      fname_starcode_out = fname_gem_mapped + '_starcode.txt'
   p1 = subprocess.Popen(['cut', '-f1', fname_gem_mapped],
         stdout=subprocess.PIPE)
   p2 = subprocess.Popen(['starcode','-t4', '-o', fname_starcode_out ],
         stdin=p1.stdout, stdout=subprocess.PIPE)
   p2.communicate()
   return fname_starcode_out



def collect_integrations_and_write_table(fname_starcode_out, fname_gem_mapped):
   """Some info."""

   KEEP = ('2L', '2R', '3L', '3R', '4', 'X','pT2')

   def dist(intlist):
      intlist.sort()
      try:
         if intlist[0][0] != intlist[-1][0]: return float('inf')
         return intlist[-1][1] - intlist[0][1]
      except IndexError:
         return float('inf')

   canonical = dict()
   with open(fname_starcode_out) as f:
      for line in f:
         items = line.split()
         for brcd in items[2].split(','):
            canonical[brcd] = items[0]

   fname_insertions_table = re.sub(r'_[^_]+$', '_insertions.txt',
          fname_gem_mapped)
   # Substitution failed, append '_insertions.txt' to avoid name collision.
   if fname_insertions_table == fname_gem_mapped:
       fname_insertions_table = fname_gem_mapped + '_insertions.txt'

   counts = defaultdict(lambda: defaultdict(int))
   with open(fname_gem_mapped) as f:
      for line in f:
         items = line.split()
         try:
            barcode = canonical[re.sub(r':[^:]+$', '', items[0])]
         except KeyError:
            continue
         if items[3] == '-':
            position = ('', 0)
         else:
            pos = items[3].split(':')
            position = (pos[0], int(pos[2]), pos[1])
            counts[barcode][position] += 1
      
   integrations = dict()
   for brcd,hist in counts.items():
       total = sum(hist.values())
       top = [pos for pos,count in hist.items() if count > max(1, 0.1*total)]
       if dist(top) > 10: continue
       ins = max(hist, key=hist.get)
       integrations[brcd] = (ins, total)

   with open(fname_insertions_table, 'w') as outf:
      for brcd in sorted(integrations, key=integrations.get):
         (chrom,pos,strand),total = integrations[brcd]
         if chrom not in KEEP: continue
         outf.write('%s\t%s\t%s\t%d\t%d\n' % (brcd,chrom,strand,pos,total))

   return
   # Done.


def main(fname1, fname2):
   fname_fasta_tomap = extract_reads_and_write_fasta_file(fname1, fname2)
   mapped_fname = call_gem_mapper(fname_fasta_tomap)
   fname_starcode_out = call_starcode(mapped_fname)
   collect_integrations_and_write_table(fname_starcode_out, mapped_fname)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
