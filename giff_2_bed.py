import sys

with open(sys.argv[1]) as f:
    for line in f:
        items = line.split()
        if not len(items) == 9: pass
        chrom = items[0]  
        start = items[3] if items[3] != '.' else int(items[4]) - 1x
        end   = items[4]
        state = items[5]
        out = (chrom,start,end,str(state))
        sys.stdout.write('%s\t%s\t%s\t%s\n' % out)
