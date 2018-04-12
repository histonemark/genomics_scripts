#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Imports
import sys

# Uniform chromosome naming
dic = {'chr2L':'2L', 'chr2R':'2R', 'chr3L':'3L', 'chr3R':'3R', 'chr4':'4', 'chrX':'X'}

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

# Opening file, replacing chromosome name

with open(sys.argv[1]) as f:
    for line in f:
        items = line.split('\t')
        if int(items[3]) > 0:
           chromosome = replace_all(items[0],dic)
           sys.stdout.write('%s\t%s\n' % (chromosome, items[1]))

# import re
# with open(sys.argv[1]) as f:
#   for line in f:
#      sys.stdout.write(re.sub('chr', '', line))
