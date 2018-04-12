import sys

with open(sys.argv[1]) as f:
   for line in f:
      try:
         chr1 = line.split()[0].split(';')[0].split(':')[0]
         chr2 = line.split()[0].split(';')[1].split(':')[0]
      except IndexError:
         sys.stderr.write('Shity line, %s\n' % line)
            
      if chr1 == chr2 == '2L':
         try:
            coor1 = line.split()[0].split(';')[0].split(':')[1]
            coor2 = line.split()[0].split(';')[1].split(':')[1]
            value = line.split()[1]
            out = (coor1,coor2,value)
            sys.stdout.write('%s\t%s\t%s\n' % out)
         except IndexError:
            sys.stderr.write('Shity line, %s\n' % line)
           