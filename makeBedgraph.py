import sys
import math

# We first write the header of the file
ttype = 'track type=bedGraph'
tname = 'name=' + sys.argv[1].split('/')[-1][:-4]
tvisi = 'visibility=full'
tcolr = 'color=200,100,0'
headr = (ttype,tname,tvisi,tcolr)
sys.stdout.write('%s\t%s\t%s\t%s\n' % headr)

# # We write the integations and their value
with open(sys.argv[1]) as f:
    f.readline() # Get rid of the header
    for line in f:
        items = line.split()
        chrom = 'chr' + items[1]
        start = items[3]
        end   = int(start) + 1
        exprs = items[-1]
        out  = (chrom,start,end,exprs)
        sys.stdout.write('%s\t%s\t%s\t%s\n' % out)

# For the endogenous genes
# with open(sys.argv[1]) as f:
#     f.readline() # Get rid of the header
#     for line in f:
#         items = line.split()
#         chrom = 'chr' + items[0]
#         start = items[1]
#         end   = items[2]
#         nexp  = items[3]
#         sys.stdout.write('%s\t%s\t%s\t%s\n' % (chrom,start,end,nexp))