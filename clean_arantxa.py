import sys

with open(sys.argv[1]) as f:
    f.readline()
    for line in f:
        if not line.rstrip().split(',')[3] == '0':
            whole = line.rstrip().split(',')
            crom = whole[0].split('"')[1]
            start = whole[1].split('.')[0]
            end = int(start) + 1
            exp = float(whole[2]) / float(whole[3])
            sys.stdout.write('chr%s\t%s\t%s\t%f\n' % \
                             (crom,start,end,exp))
