import sys
import pdb
#pdb.set_trace()

ncontacts = 0
nhaploA   = 0
nhaploB   = 0
hetero    = 0

with open(sys.argv[1]) as f:
   for line in f:
      ncontacts += 1
      pair1,pair2 = line.rstrip().split(';')
      haplo1 = pair1.split('_')[1]
      haplo2 = pair2.split('_')[1]
      if haplo1 == haplo2 == 'A':
         nhaploA += 1
      elif haplo1 == haplo2 == 'B':
         nhaploB += 1
      else:
         hetero += 1

   sys.stdout.write('Total number of contacts: %s\n' % ncontacts)
   sys.stdout.write('Number of contacts type A: %s\n' % nhaploA)
   sys.stdout.write('Number of contacts type B: %s\n' % nhaploB)
   sys.stdout.write('Number of intrachromosomal contacts : %s\n' % hetero)
   recovered = ncontacts - (nhaploA + nhaploB + hetero)
   sys.stdout.write('Ill do it for you: total - assigned = %s\n' % \
                    str(recovered)) 