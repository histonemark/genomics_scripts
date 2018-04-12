import os
import re
import subprocess
import sys
import tempfile

from collections import defaultdict


def call_starcode_on_mapped_file(fname_gem_mapped):
   """This function takes the barcodes contained in the first column of
   the mapped file and feed's them to starcode that clusters them."""

   fname_starcode = re.sub(r'\.map$', '_starcode.txt', fname_gem_mapped)
   # Substitution failed, append '_starcode.txt' to avoid name collision.
   if fname_gem_mapped == fname_starcode:
      fname_starcode = fname_gem_mapped + '_starcode.txt'

   # Skip if file exists.
   if os.path.exists(fname_starcode): return fname_starcode
  
   # it to starcode.
   p1 = subprocess.Popen(['cut', '-f1', fname_gem_mapped],
         stdout=subprocess.PIPE)
   p2 = subprocess.Popen(['starcode','-t4','-d2','--print-clusters', '-o', fname_starcode],
         stdin=p1.stdout, stdout=subprocess.PIPE)
   # 'communicate()' returns a tuple '(stdoutdata, stderrdata)'.
   # If 'stderrdata' is not None we notify to know where the problem arose.
   stdoutdata,stderrdata = p2.communicate()
   if stderrdata is not None:
      sys.stderr.write("Pipe error (%s)\n" % str(stderrdata))
   return fname_starcode


def collect_integrations(fname_starcode_out, fname_gem_mapped):
   """This function reads the starcode output and changes all the barcodes
   mapped by their canonicals"""         
         
   canonical = dict()
   with open(fname_starcode_out) as f:
      for line in f:
         items = line.split()
         for brcd in items[2].split(','):
            canonical[brcd] = items[0]

   integrations = defaultdict(lambda: defaultdict(int)) 
   with open(fname_gem_mapped) as f:
      for line in f:
         items = line.split()
         try:
            barcode = canonical[items[0]]
         except KeyError:
            continue
         try:
            # Keep only the first 3 items (chr, strand, pos).
            pos = items[3].split(':')[:3]
            pos[2] = int(pos[2]) if pos[1] == '+' else int(pos[2]) + len(items[1])
         except IndexError:
            pos = ('NA',)
         integrations[barcode][tuple(pos)] += 1
         
   return integrations

def compare_read1_and_read2(integrations_read1, integrations_read2):
   """Compare mapped positions for read1 and read2, identify trapping
   events."""
   
   # Define a local function.
   def dist(intlist):
      """Macro to compute distances."""
      intlist.sort()
      try:
         if intlist[0][0] != intlist[-1][0]: return float('inf')
         return int(intlist[-1][2]) - int(intlist[0][2])
      except IndexError:
         return float('inf')
   
   assert(len(integrations_read1) == len(integrations_read2))
   
   for barcode in sorted(integrations_read1):
      lugares_1 = integrations_read1[barcode]
      lugares_2 = integrations_read2[barcode]
      # Get the total number of reads for this barcode.
      total_reads_1 = sum(lugares_1.values())
      total_reads_2 = sum(lugares_2.values())
      assert(total_reads_1 == total_reads_2)
      # Start with read 2.
      top_2 = [pos for pos,count in lugares_2.items() \
         if count > max(1, 0.1*total_reads_2)]
      if dist(top_2) > 10:
         # Barcode inserted at different loci.
         # Write stuff here.
         continue
      insertion_point = max(lugares_2, key=lugares_2.get)
      sys.stdout.write(barcode)
      sys.stdout.write('\t%s\t%s\t%d\t' % insertion_point)
      # Now check if read 1 is nearby.
      top_1 = [pos for pos,count in lugares_1.items() \
         if count > max(1, 0.1*total_reads_1)]
      if dist(top_1) < 10:
         # Only 1 ligation point.
         ligation_point = max(lugares_1, key=lugares_1.get)
         distance = dist([ligation_point, insertion_point])
         if distance < 1500:
            # Non trapping event for this barcode.
            sys.stdout.write('A\t%d\t%d\n' % (distance, total_reads_2))
         else:
            # Trapping event.
            sys.stdout.write('B\tNA\t%d\n' % total_reads_2)
      else:
         # More than 1 ligation points. Go through all the
         # ligation points in 'top_1', compute their distance
         # to the insertion point.
         trapping_only = True
         for top in top_1:
            if dist([top, insertion_point]) < 1500:
               sys.stdout.write('C\tNA\t%d\n' % total_reads_2)
               trapping_only = False
               break
         if trapping_only:
            sys.stdout.write('D\tNA\t%d\n' % total_reads_2)


starcode_fname = call_starcode_on_mapped_file(sys.argv[1])
integrations_read_1 = collect_integrations(starcode_fname, sys.argv[1])
integrations_read_2 = collect_integrations(starcode_fname, sys.argv[2])
compare_read1_and_read2(integrations_read_1, integrations_read_2)
