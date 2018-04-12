import sys

GET = ['2L','2R','3L','3R','4','X']
with open(sys.argv[1]) as f:
   f.readline()
   for line in f:
      items = line.split()
      chrom = items[0][3:]
      start = items[1]
      if int(items[3]) > 0 and chrom in GET:
         sys.stdout.write('%s\t%s\t%s\n'
                          % (chrom,int(start)-1000,start))
      elif int(items[3]) < 0 and chrom in GET:
          sys.stdout.write('%s\t%s\t%s\n'
                          % (chrom,start,int(start)+1000))
      