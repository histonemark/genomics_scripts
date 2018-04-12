import sys

with open(sys.argv[1],'r') as f:
   for line in f:
      items = line.split()
      chrom = items[0]
      # 0 based coordinate
      posit = int(items[1]) 
      snp1  = items[2] 
      snp2  = items[3]
      mask = len(snp1) if len(snp1) > len(snp2) else len(snp2) 
      sys.stdout.write('%s\t%d\t%d\n' % (chrom,posit,posit + mask))