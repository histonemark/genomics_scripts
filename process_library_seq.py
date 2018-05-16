#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import sys

from gzopen import gzopen

# The processing relies on the correct naming of the promoters by the user.
# The script must be called inside the `/Basecalls` directory after bcl2fastq

# To know how many files we have to process we match each Sample of the first lane.
# Samples are called: PromoterA12_S12_L001_R1_001.fastq.gz ... PromoterA12_S12_L003_R1_004.fastq.gz
fn_re = re.compile(r'Promoter[A-H][0-9][0-2]?_S[0-9][0-2]?_L001')
samples = [f for f in os.listdir('.') if
           fn_re.match(f)]
# The reads from the qMiseq come separated in 4 lanes. Merge them.

for sample in samples:
    # Ex. PromoterA12_S12_L001_R1_001.fastq.gz
    fn_items = sample.split('_')
    outfname = fn_items[0] + '.fastq'
    if os.path.isfile(outfname):
            sys.stdout.write("Sample: %s already processed, skiping.\n"
                             % outfname.split('/')[-1])
            continue

    lanes = ['L001','L002','L003','L004']
    for lane in lanes:
        if lane == 'L001':
            toextract = '_'.join([fn_items[0],fn_items[1],lane,
                                  fn_items[3],fn_items[4]])
            with gzopen(sample) as f, open(outfname,'w') as g:
                for line in f:
                    g.write(line)
        else:
            toextract = '_'.join([fn_items[0],fn_items[1],lane,
                                  fn_items[3],fn_items[4]])
            with gzopen(sample) as f, open(outfname,'a') as g:
                for line in f:
                    g.write(line)
                
        
        
    
