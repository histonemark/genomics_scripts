#!/usr/bin/env python

import sys

# Drosophila Chromosome lenghths from BDGP R5/dm3 Apr. 2006
# Not including the het, M  and Uextra = 38'305'954 ~ 23% of Genome
chr_lenghts = {'chr2L':23011544,'chr2R':21146708, 'chr3L':24543557,
               'chr3R':27905053, 'chr4':1351857, 'chrX':22422827,
               'chrU':10049037}

# Let's create 200bp windows of each chromosomes and print a tsv

for name,size in chr_lenghts.iteritems():
    n_bins = int(size / 200)
    remain = int(size % 200)
    for i in range(n_bins):
        start = i * 200 + 1
        end   = start + 199
        out = (name, start, end)
        sys.stdout.write('%s\t%d\t%d\n' % out)
    if remain != 0:
        out2 = (name,end + 1,end + remain)
        sys.stdout.write('%s\t%d\t%d\n' % out2)
