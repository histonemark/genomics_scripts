import sys
import re

GET = ['2L','2R','3L','3R','4','X']

with open(sys.argv[1]) as f:
   for i in range(5):
      f.readline()
   for line in f:
      items = line.split()
      if items[2] == 'gene' and items[0] in GET:
         chrom = items[0]
         start = items[3]
         stop  = items[4]
         strand = items[6]
         name  = re.sub(r'["\\;]','',items[9])
         sys.stdout.write('%s\t%s\t%s\t%s\t%s\n'
                          % (chrom,start,stop,strand,name))
   