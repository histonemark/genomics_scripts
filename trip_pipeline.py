import sys
import re


# The data input from the sequencing facility comes in a directory of the date.
# For analizing a iPCR experiment copy the fastq.gz of the dated directory to 
# a directory called iPCR_Trip_name
# In the case of the gDNA and cDNA both directories have to be available so copy# the content of *both* cDNA and gDNA fastq.gz to a directory called cgdna_Trip_#name. 


def check_type_experiment(directory):
    '''There are 3 types of experiment reads: From gDNA, cDNA or iPCR '''

    type_of_experiment = ''

    if sys.argv[1] == 'ipcr':
        type_of_experiment = ipcr
    elif sys.argv[1] == 'cgdna':
        type_of_experiment = cgdna
    else: print 'Please chose an argument ipcr,gdna or cdna'    
        
    return type_of_experiment
    

def get_names_indexes(list_files):
    ''' This function check's how many different experiments are sequenced '''
    if type_of_experiment == ipcr:
        pass
    elif type_of_experiment == cgdna:
    
    return

def do_starcode(files):
    ''' Call starcorde on each of the files to get the barcode and reads '''
    
