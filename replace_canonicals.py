#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import pdb 
from collections import defaultdict

MAPPED = [fname for fname in os.listdir(".") if \
          fname.split("_")[-1] == "mapped.txt"]


for fname in MAPPED:
   print('Processing sample %s' % fname)

   # Lets build the dictionary of canonicals for this Sample
   canonicals = dict()
   can_fname =  "_".join([fname.split("_")[0],"canonicals.txt"]) 
   with open(can_fname) as f:
      for line in f:
         canonical,count,bcds = line.split()
         canonicals[canonical] = canonical
         for bcd in bcds.split(","):
            canonicals[bcd] = canonical

   def dist(intlist):
      intlist.sort()
      try:
         if intlist[0][0] != intlist[-1][0]: return float('inf')
         return intlist[-1][1] - intlist[0][1]
      except IndexError:
         return float('inf')
   
   # Aggregate the counts and change barcode for its canonical         
   counts = defaultdict(lambda: defaultdict(int))
   with open(fname) as g:
      for line in g:
         items = line.split()
         try:
            barcode = canonicals[items[0]]
         except KeyError:
            continue
         
         chrom = items[1]
         loc = int(items[2]) 
         position = (chrom, loc)
         counts[barcode][position] += 1
      
   integrations = dict()
   for brcd,hist in counts.items():
       total = sum(hist.values())
       top = [pos for pos,count in hist.items() \
             if count > max(1, 0.1*total)]
       # Skip barcode in case of disagreement between top votes.
       if dist(top) > 10: continue
       ins = max(hist, key=hist.get)
       integrations[brcd] = (ins, total)

   outfname = "_".join([fname.split("_")[0],"insertions_table.txt"])    
   with open(outfname, 'w') as outf:
      for brcd in sorted(integrations, key=lambda x: (integrations.get(x),x)):
         (chrom,pos),total = integrations[brcd]
         outf.write('%s\t%s\t%d\t%d\n' % (brcd,chrom,pos,total))
