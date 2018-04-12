import sys
import pdb

def keep_or_not(pair1,pair2):
   items1 = pair1.split()
   items2 = pair2.split()
   if len(items1) < 14 or len(items2) < 14:
      # Non mapped one or both
      return 0
   #pdb.set_trace()
   # Keep the haplotype if AS != XS otherwise only loc
   AS1 = int(items1[13].split(':')[2])
   XS1 = int(items1[14].split(':')[2])
   AS2 = int(items2[13].split(':')[2])
   XS2 = int(items2[14].split(':')[2])
   # cases
   if AS1 == XS1 and AS2 == XS2:
      return 0
   elif AS1 > XS1 and AS2 == XS2:
      # Impute haplo from fwd read
      haplo   = items1[2].split('_')[1] 
      contact = items1[2] + ';' + items2[2][:-2] + '_' + haplo
      sys.stdout.write(contact + '\n')
   elif AS1 == XS1 and AS2 > XS2:
      # Impute haplo from rev read
      haplo = items2[2].split('_')[1]
      contact = items2[2] + ';' + items1[2][:-2] + '_' + haplo
      sys.stdout.write(contact + '\n')
   else:
      contact = items1[2] + ';' +  items2[2]
      sys.stdout.write(contact + '\n')
   
      
# Paired-end reads from bwa are in different lines (sam)
pair = 0
fwd = ''
rev = ''
with open(sys.argv[1]) as f:
   for line in f:
      if not line[:3] == 'SRR': continue
      #pdb.set_trace()
      if pair == 0:
         fwd = line
         pair += 1
      elif pair == 1:
         rev = line
         if fwd.split()[0] != rev.split()[0]:
            # This is due to a 3d match, skip it.
            fwd = rev
            pair = 1
             
         keep_or_not(fwd,rev)
         pair = 0
         fwd  = ''
         rev  = ''