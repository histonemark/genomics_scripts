import sys

GET = ['2L','2R','3L','3R','4','X']

with open(sys.argv[1]) as f:
   for line in f:
      items = line.split()
      if items[4][3:] not in GET:
         continue
      else:
         chrom = items[4][3:]
         start = items[5]
         stop  = items[6]
         sys.stdout.write('%s\t%s\t%s\n'
                          %(chrom,start,stop))