import sys
    
seq = ''

with open(sys.argv[1],'r') as f:
   # Directly print the first line 
   sys.stdout.write(f.readline())
   for line in f:
      if line[0] == '>': sys.stdout.write('\n'+line)
      else: sys.stdout.write(line.rstrip())
