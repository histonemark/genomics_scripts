#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import pdb

#pdb.set_trace()
for fnamemap in os.listdir("."):
    try:
        sample = fnamemap.split(".")
        if sample[1] == "sam":
            outfname = sample[0] + "_mapped.txt"
            with open(outfname,"w") as f, open(fnamemap) as g:
                for line in g:
                    if line[0] == "@": continue
                    items = line.split()
                    if int(items[4]) >= 20:
                        # Write barcode and mapping position
                        f.write("\t".join([items[0],items[2],items[3],"\n"]))
    except IndexError:
        continue
