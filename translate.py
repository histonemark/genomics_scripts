import re
import sys

from collections import defaultdict

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

def translate(txt):
    return ''.join([gencode.get(txt[i:(i+3)], '_') for i in range(0,len(txt),3)])

counts = defaultdict(int)
pattern = r'CCACTGAAGACTGC([GATCN]+)GAGGCCCTAGGGGCC'
with open(sys.argv[1]) as f:
   for line in f:
      items = line.split()
      variant_seq = re.search(pattern, items[0]).groups()[0]
      protseq = translate(variant_seq)
      variant_count = int(items[1])
      counts[protseq] += variant_count

for protseq,count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
   sys.stdout.write('%s\t%d\n' % (protseq,count))
