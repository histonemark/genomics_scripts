# Change chromosome names to be BED compliant 'chr3L'

import sys

# Add 'chr' to first column of each line of the file (chromosome name 3L)
# Ex line '3L	11245410	11246409	+	FBgn0041094'
# Out line 'chr7    127471196  127472363  name  0  +' (BED)
with open(sys.argv[1]) as f:
    for line in f:
        coord = '\t'.join(line.split('\t')[1:3])
        column1 = str('chr') + line.split('\t')[0]
        strand = line.split('\t')[3]
        name = line.rstrip().split('\t')[4]
        # Write new line respecting BED format
        new_line = '%s\t%s\t%s\t999\t%s\n' % (column1, coord, name, strand)
        sys.stdout.write(new_line)
