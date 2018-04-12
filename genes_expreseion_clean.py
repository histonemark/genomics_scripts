import sys

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('FB'):
            items = line.split()
            gene     = items[0]
            chrom    = items[1]
            start    = items[2]
            end      = items[3]
            value    = items[10]
            out      = (chrom,start,end,value,gene)
            sys.stdout.write('%s\t%s\t%s\t%s\t%s\n' % out)
