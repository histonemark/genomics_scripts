import sys

# This is a simple parser to transform te file with the overlap of
# modENCODE TSS Black domains and silent in Kc157 to bed for UCSC GB

# Let's open a file to write to.
g = open('./silent_blue_tss_2GB.txt','w')

# Let's open the results of the overlap done in R.

with open(sys.argv[1]) as f:
    f.readline() # To get rid of the header line.
    for line in f:
        items = line.split()
        chr = items[0]
        stt = items[1]
        end = items[2]
        nam = items[6]
        scr = (int(items[5]))
        out = (chr,stt,end,nam,scr)
        g.write('%s\t%s\t%s\t%s\t%d\n' % out)
    g.close()
