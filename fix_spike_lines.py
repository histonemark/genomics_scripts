#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys




with open(sys.argv[1]) as f:
   for line in f:
      items = line.split()
      if items[0] == '0':
         sys.stdout.write(line)
      elif items[0] == '#':
         sys.stdout.write(line)
      elif items[1] != 'spike':
         sys.stdout.write(line)
      elif items[1] == 'spike':
         kip = line
         continue
      else:
         sys.stdout.write('%s\n' % (keep.rstrip() + ' ' + line))
        
     