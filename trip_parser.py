#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from gzopen import gzopen
import subprocess
import os
from automata import PatternMatcher


wd = os.getcwd()

seq_files = []
def get_files(directory):
    ''' This function iterates over the directory where it has been called and takes the files with extension .fastq.gz and adds the to a list''' 
    for f in os.listdir(wd):
        if f.endswith("fastq.gz"):
            seq_files.append(f)
    return seq_files


def get_bcd(list):
   '''This fuction cuts the sequencing read to get the barcode and outputs to an txt file. It does so for normal and spike reads'''

   for fastq in seq_files:
      current = os.path.join(wd,fastq)
      spike_out = open(fastq.split('.')[0] +'_spike.txt','w')
      bcds_out  = open(fastq.split('.')[0] + '_barcodes.txt','w')
      GFP = PatternMatcher('CATGCTAGTTGTGGTTTGTCCAAACT', 3)
      spike = PatternMatcher('CATGATTACCCTGTTATC', 2)
      with gzopen(current) as f:
         sys.stderr.write('Currently processing %s\n' %current)
         for lineno,line in enumerate(f):
            if lineno % 4 != 1: continue
            pos = GFP.start(line)
            if pos > -1:
                if 14 <= pos <= 24: bcds_out.write(line[:pos] + '\n')
            else:
                pos = spike.start(line)
                if pos > -1:
                    if 14 <= pos <= 24: spike_out.write(line[:pos] + '\n')
                else: continue
   spike_out.close()
   bcds_out.close()


# Now we need to call starcode on each processed file.

files_to_starcode = []        
def get_files_bcd(directory):
    ''' This function take's the processed files and puts them in a list to be clustered by starcode'''

    for f in  os.listdir(wd):
        if '_spike' in f or '_barcodes' in f:
            files_to_starcode.append(f)
    return files_to_starcode
    
            
def starcode_em(list):
    ''' This function calls starcode on each file _spike or _barcodes by default using 4 cores. There will be implemention to use it with less cores.'''

    for f in files_to_starcode:
        current  = os.path.join(wd,f)
        out_file = str(current[:-4]) + '_starcoded.txt'
        subprocess.call(['starcode','-t4','-i',current,'-o',out_file])
        print 'Starcoding file %s' % current


if __name__ == '__main__':

    get_files(wd)
    get_bcd(seq_files)
    get_files_bcd(wd)
    starcode_em(files_to_starcode)
    
