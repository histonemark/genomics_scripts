import sys

letters =  ['A','B','C','D','E','F','G','H']
columns =  [i+1 for i in range(12)]
iter = 0

with open(sys.argv[1]) as f:
    for line in f:
        letter = letters[0]
        iter += 1
        items = line.split(',')
        name = items[0]
        fwd  = items[1]
        rev  = items [2]
        sys.stdout.write('%s%d,%s,%s,%s' % (letter,iter,name,fwd,rev))
        if iter == 12:
            letters = letters[1:]
            iter = 0
        
        
