#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

# Uniform chromosome naming
dic = {'chr2L':'2L', 'chr2R':'2R', 'chr3L':'3L', 'chr3R':'3R', 'chr4':'4', 'chrX':'X'}
# Only accepts bed files so we need to change from 3L notation to chr3L
def replace_all(text, dic):
   for i, j in dic.iteritems():
      text = text.replace(j, i)
   return text

# Opening file, replacing chromosome name.
with open(sys.argv[1]) as f:
   for line in f:
      items = line.split('\t')[:4]
      chromosome = replace_all(items[1],dic)
      if items[3] == '-':
        rest_of_line = '%s\t%s\t%d\t-%s\n' % (chromosome, items[2], int(items[2])+999, items[0])
        sys.stdout.write(rest_of_line)
      else:
        rest_of_line = '%s\t%d\t%s\t+%s\n' % (chromosome, int(items[2])-999, items[2], items[0])
        sys.stdout.write(rest_of_line)
        


















        # More Pythonic
        #Python 2.7.3 (default, Sep 26 2012, 21:53:58) 
        #[GCC 4.7.2] on linux2
        #Type "help", "copyright", "credits" or "license" for more information.
        #>>> L = ['2L', '2L', '3R']
        #>>> L
        #['2L', '2L', '3R']
        #>>> ['chr' + a for a in L]
        #['chr2L', 'chr2L', 'chr3R']
        #>>> ['chr' + element for element in L]
        #['chr2L', 'chr2L', 'chr3R']


