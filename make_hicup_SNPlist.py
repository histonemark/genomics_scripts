import sys

# Transforms a bed list of SNPs to a SNPsplit compatible input file

with open(sys.argv[1]) as f:
   for lineno,line in enumerate(f):
      ide = lineno
      items = line.split()
      chrom = items[0][3:]
      pos   = int(items[1])
      alA   = items[2]
      alB   = items[3]
      val   = len(alA) if len(alA) > len(alB) else len(alB)
      out = (ide,chrom,pos,val,alA,alB)
      sys.stdout.write('%s\t%s\t%s\t%s\t%s/%s\n' % out)