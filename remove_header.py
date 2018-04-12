import sys

with open(sys.argv[1]) as f:
   for line in f:
      items = line.split()
      if items[0] == 'barcode':
         continue
      else:
         sys.stdout.write(line)
         