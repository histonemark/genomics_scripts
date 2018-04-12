#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import pdb

#pdb.set_trace()
EXECFNAME = "mapall.sh"
GENOME= "/mnt/shared/seq/bwa/dm4R6/dmel-all-chromosome-r6.15.fasta"

with open(EXECFNAME,"w") as f:
    for fname in os.listdir("."):
        try:
           samplefname = fname.split(".")  
           if samplefname[1] == "tomap":
               mapoutfname = samplefname[0] + ".sam"  
               f.write(" ".join(['bwa mem -t4', GENOME, fname, ">", \
               mapoutfname, "&\n"]))    
        except IndexError:
            continue
