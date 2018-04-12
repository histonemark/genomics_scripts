#!/usr/bin/env python
# -*- coding:utf-8 -*-

# We need the module 'sys' to print text to stdout.
import sys


# Special assignment to 'f' because it is a file.
GATC_Primers = {}
with open(sys.argv[1]) as f:
   for line in f:
       if '<' in line:
           Primer_name = line.split(';')[1]
           Primer_sequence = line.split(';')[2].split()[0][:-1].upper()
           GATC_Primers[Primer_name] = Primer_sequence

print GATC_Primers

