import sys

header = ['track type=wiggle_0',
          'name='+'"' + sys.argv[1] + '"',
          'description= TRiP',
          'visibility=full',
          'color=200,100,0',
          'altColor=0,100,200',
          'priority=3']

with open(sys.argv[1]) as f:
    f.readline()
    print ' '.join(header)
    for line in f:
        items = line.split()
        chrom = 'chr' + items[1]
        start = items[3]
        end   = int(items[3]) + 1
        expr  = items[-2]
        sys.stdout.write('%s\t%s\t%s\t%s\n'
                         % (chrom,start,end,expr))