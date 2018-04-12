import sys

with open(sys.argv[1]) as f:
    for line in f:
        if line[0] is '@': continue
        items  = line.split()
        if items[4] < 20: continue
        chrom  = items[2]
        pos    = items[3]
        strand = '-' if int(items[1]) & 16 else '+'
        if chrom != '2L': continue
        if 12455540 < int(pos) < 12546611:
            out = (chrom,pos,strand)
            sys.stdout.write('%s\t%s\t%s\n' % out)
        