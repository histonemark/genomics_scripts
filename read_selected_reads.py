import sys


# Tuples encoding the genes
genes = [('2L',16798525,16801584) ,('2L',20829107,20831063),('2R',10102740,10104077),
 ('2R',10657443,10660135),('3L',5647281,5650484),('3L',11244909,11248343),
 ('3R',17695905,17699362),('3R',13360210,13362858),('X',1751922,1753326),
 ('X',20913012,20915134)]

# Read the RNA mappings and keep the reads mapping to the red genes
with open(sys.argv[1]) as f:
    for line in f:
        try:
            items = line.split()
            chrom = str(items[-1].split(':')[0])
            pos   = int(items[-1].split(':')[2])
            strnd = items[-1].split(':')[1]  
            for gene in genes:
                if gene[:2] <= (chrom,pos) <= gene[::2]:
                    if strnd == '+':
                        out = (chrom,pos,pos)
                        sys.stdout.write('chr%s\t%s\t%s\n' % out)
                    else:
                        out = (chrom,pos - 50, pos - 50)
                        sys.stdout.write('chr%s\t%s\t%s\n' % out)
        except IndexError: continue