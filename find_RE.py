import sys
import pdb


# -R-estriction -S-ites -D-ictionary
RSD = {}

# Populate the dict
with open('all_RE.tsv') as f:
    for line in f:
        key,val = line.rstrip().split()[::-1]
        RSD[key] = val
# Negative and positive controls
RSD['negative_cont'] = 'ZZZZZZZZ'
RSD['positive_cont'] = 'AA'



seqs = []
with open(sys.argv[1]) as g:
    g.readline() # Trash first fasta header
    seq = ''
    for line in g:
        if line[0] == '>': 
            seqs.append(seq)
            seq = ''
        else:
            seq = seq + line.rstrip()


# # Check REsites in each sequence
# for k in RSD:
#     for seq in seqs:
#         if RSD[k] in seq:
#             continue # Test more seqs
#         else:
#             break # Try other RE if not found.
#     else:
#         sys.stdout.write('Candidate found: %s\n' % k)

# Lets check how many promoters we cut with
# each restriction enzyme.

# Check number REsites in each sequence
for k in RSD:
    nhits = 0
    for seq in seqs:
        if RSD[k] in seq:
            nhits += 1
    else:
        sys.stdout.write('RE %s has %s\n' % (k,nhits))
        nhits = 0
