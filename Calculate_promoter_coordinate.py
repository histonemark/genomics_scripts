#!/usr/bin/env python
# -*- coding:utf-8 -*-

# We need the module 'sys' to print text to stdout.
import sys
# Special assignment to 'f' because it is a file.
with open(sys.argv[1]) as f:
   for line in f:
      #if not line.startswith('chr'): continue
      if line[:3] != 'FBg': continue
      items = line.split('\t')
      if items[3] == '-':
         newline = '%s\t%d\t%s\t%s\t%s\n' % (items[1], int(items[2])-999, items[2], items[3], items[0])
         sys.stdout.write(newline)
      else:
         newline = '%s\t%s\t%d\t%s\t%s\n' % (items[1], items[2], int(items[2])+999, items[3], items[0])
         sys.stdout.write(newline)
