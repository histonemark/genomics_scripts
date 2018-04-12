# -*- coding:utf-8 -*-
# Parser to upload the file to genome browser with chr startUTR endUTR
# Genome browser uses bed file format
# chr7    127471196  127472363

import sys

# With the counter the code is reusable for each file that has a header
counter = 0

with open('gene_per_TSS.txt') as f:
    for line in f:
        counter = counter + 1 
        if counter > 1:
            new_line = line.split()
            chr_name = new_line[0]
            start_utr = new_line[5]
            end_utr = new_line[6]
            strand = new_line[2]
            to_write = chr_name, start_utr, end_utr, strand
            sys.stdout.write('chr%s\t%s\t%s\tTSSperUTR\t389\t%s\n' % (to_write))
