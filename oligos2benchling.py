import re
import sys

# Benchling has ability to upload all the primers
# but doesn't allow all the characters that we use

def compatible_seq(fline):
    '''Takes a line from oligoz file and returns a name, 
a sequence and a comment'''
    items = fline.rstrip().split()
    seq   = items[1]
    # Ridiculous amounts of ways to say phospho
    phos  = re.compile(r'\[?P\s*-*')
    # Delimiting caracters
    delim = re.compile(r'[\[\]\?\#]')
    # Non DNA characters
    
with open(sys.argv[1]) as f:
    for line in f:
        items = line.split()
        name  = items[0]
        seq, description = clean_seq()


        
