# Imports

import sys

# Open the file, read line by line and write strand and score dependig if column 3 is positive or negative
with open(sys.argv[1]) as f:
   for line in f:
      elements = line.split()  
      if int(elements[3]) > 0:
        new_line = '%s\t%s\t%s\t+\t%s\n' % (elements[0], elements[1], elements[2], elements[3])
        sys.stdout.write(new_line)
      else:  
         new_line = '%s\t%s\t%s\t-\t%s\n' % (elements[0], elements[1], elements[2], abs(int(elements[3])))
         sys.stdout.write(new_line)
