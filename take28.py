#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

with open(sys.argv[1]) as f:
   for line in f:
      if line[0] == '>': sys.stdout.write(line)
      else: sys.stdout.write(line.rstrip()[:28] + '\n')
