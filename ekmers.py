import sys
from collections import defaultdict

k = 10

T = {
   'A': 'T',
   'T': 'A',
   'G': 'C',
   'C': 'G',
}

def rc(txt):
   return ''.join([T[a] for a in txt[::-1]])

counter = defaultdict(int)
with open(sys.argv[1]) as f:
   for line in f:
      if line[0] == '>': continue
      for i in range(len(line)-k):
         counter[line[i:i+k]] += 1

for kmer,count in counter.items():
   sys.stdout.write('%s\t%d\n' % (kmer,count))
   sys.stdout.write('%s\t%d\n' % (rc(kmer), count))
