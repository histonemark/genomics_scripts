import sys

BL = open('Black_promoters.txt','wb')
BU = open('Blue_Promoters.txt','wb')
RD = open('Red_Promoters.txt','wb')
YL = open('Yellow.promoters','wb')
GR = open('Green_promoters','wb')

with open(sys.argv[1]) as f:
    for line in f:
        items  = line.split()
        chrom  = items[0]
        start  = int(items[1])
        end    = int(items[2])
        strand = items[3]
        color  = items[5]
        if strand == '+':
           promoters = start - 500
           promotere = start
        else:
           promoters = end
           promotere = end + 500   
        if color == 'BLACK':
           BL.write('%s\t%s\t%s\n' % (chrom,promoters,promotere))
        elif color == 'BLUE':
           BU.write('%s\t%s\t%s\n' % (chrom,promoters,promotere))
        elif color == 'RED':
           RD.write('%s\t%s\t%s\n' % (chrom,promoters,promotere))
        elif color == 'YELLOW':
           YL.write('%s\t%s\t%s\n' % (chrom,promoters,promotere))
        elif color == 'GREEN':
           GR.write('%s\t%s\t%s\n' % (chrom,promoters,promotere))
           
           