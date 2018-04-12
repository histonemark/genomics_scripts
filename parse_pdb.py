import sys

with open(sys.argv[1]) as f:
    for line in f:
        items = line.split(',')
        if items[1] == '$':
            sequence = items[2]
        elif items[1]  != '$':
            sequence = items[1]
        else: sys.stdout.write('A problem in a line!')

        name = items[0].replace(' ','_')
        number = items[3]
        out = (name,sequence,number)
        sys.stdout.write('%s\t%s\t%s' % out)
            
    
