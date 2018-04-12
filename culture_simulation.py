#!/usr/bin/env python
# -*- coding:utf-8 -*-

import heapq
import random
import sys

NINIT = 30000
NFINAL = 1000000

gamma = random.gammavariate

def main():
   random.seed(123)
   heap = []
   for i in range(NINIT):
      heapq.heappush(heap, (gamma(2,1), i))
   for i in range(NFINAL - NINIT):
      (time, idx) = heapq.heappop(heap)
      heapq.heappush(heap, (time + gamma(2,1), idx))
      heapq.heappush(heap, (time + gamma(2,1), idx))
   for (ignore,idx) in heap:
      sys.stdout.write('%d\n' % idx)


if __name__ == '__main__':
   main()
