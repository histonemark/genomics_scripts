

# Imports
import sys
import pdb

# Takes the sequences from oligos and the first number of the excel file 
# and generates a CSV to upload to sigma. 
pdb.set_trace()

# Define some variables

#oligo_name = int(raw.imput('Enter the number of the first oligo without GAT\n') -1 ) 
#scale_of_syn = ('0,025 or 0,05?')
#how_many_oligoz = int(raw.imput('How many oligoz you would like to order?\n')

# We have to generate a CSV file with the following sigma instructions.
# Oligo_name,[modif]sequence,scales of synthesis,purification,spetiasl instructions

with open(sys.argv[1]) as f:
   for line in f:
      if line[0] == '(':
         seq = line.split()[2]
         oligo_name= oligo_name + 1
         oligo = 'GAT%s,%s,%int,%s,HPLC\n' % (str(oligo_name)),seq,scale_of_syn,)  
      if oligo_name > how_many_oligoz: break 
      sys.stdout.write(oligo)
    
   
