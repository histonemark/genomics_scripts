
import sys
KEEP = frozenset([
      '2L', '2LHet', '2R', '2RHet', '3L', '3LHet',
      '3R', '3RHet', '4', 'X', 'XHet', 'U', 'Uextra', 'pT2',
   ])

def collect_integrations(fname_starcode_out, fname_gem_mapped):
   """This function reads the starcode output and changes all the barcodes
   mapped by their canonicals"""
   
   canonical = dict()
   with open(fname_starcode_out) as f:
      for line in f:
         items = line.split()
         for brcd in items[2].split(','):
            canonical[brcd] = items[0]
 
   #counts = defaultdict(lambda: defaultdict(int))
   with open(fname_gem_mapped) as f:
      for line in f:
         items = line.split()
         try:
            barcode = canonical[items[0]]
         except KeyError:
            continue
         if items[3] != '-':
            pos = items[3].split(':')
            if pos[0] in KEEP:
               chrom = pos[0]
               strand = pos[1]
            else:
               continue
            if pos[1] == '+':
               start = int(pos[2])  
            else:
               start = int(pos[2]) + len(items[1])
            sys.stdout.write('%s\t%s\t%s\t%d\n' % (barcode,chrom,strand, start))
         else:
            (chrom, strand, start) = ('NA','NA','NA')     
         sys.stdout.write('%s\t%s\t%s\t%s\n' % (barcode,chrom,strand, start))
         
collect_integrations(sys.argv[1], sys.argv[2])
