# Edyta ask's me if we could know the random sequences of the 20 random nucleotides of the barcode.

import sys
import random

bases = ['A','C','T','G']

def pick_a_base():
    selected = bases[random.randint(1,4) - 1]
    return selected

def twentimer():
    sequence =  ''

    for x in range(1,20):
        sequence = sequence + pick_a_base()
    print sequence

twentimer()



# We have 4 nucleotides and want all the combinations of twentimers wich is
# 4^20 = 1.099.511.627.776 different sequences.
