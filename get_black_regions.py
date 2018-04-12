import sys

with open(sys.argv[1]) as f:
    f.readline()
    for line in f:
        if line.split()[3] == 'BLACK':
            sys.stdout.write(line)
