#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import subprocess
import sys

import seeq

# Enter library sequencing directories and extract
# the barcodes of each Promoter to starcode them.

SUBDIR = '/Data/Intensities/BaseCalls/'
seq_dirs = [os.path.abspath(seqd) for seqd in os.listdir(".")
            if os.path.isdir(seqd)]

for sdir in seq_dirs:
    data_path = sdir + SUBDIR
    prom_fnames = [fname for fname in os.listdir(data_path)
                   if re.match(r'Promoter[A-F][0-9][0-9]?.fastq', fname)]

    # Extract the barcodes of each promoter file
    for fname in prom_fnames:
        prom_name = fname.split('.')[0]
        outfname = data_path + prom_name + '_to_starcode.txt'
        with open(data_path + fname) as f, open(outfname, 'w') as g:
            for lineno, line in enumerate(f):
                # Take sequence only.
                if lineno % 4 != 1:
                    continue
                # The read should contain backbone after the barcode
                GFP = seeq.compile('CATGCTAGTTGTGGTTTGTCCAAACTCATC', 7)
                found_seq = GFP.match(line.rstrip())
                if not found_seq:
                    continue
                g.write("%s\n" % line[:20])

    # Starcode each Promoter barcode file
    regexp = "r'Promoter[A-F][0-9][0-9]?_to_starcode.txt'"
    starcodefn = [fname for fname in os.listdir(data_path) if
                  re.match(regexp, fname)]
    for fname in starcodefn:
        outfname = data_path + fname.split('_')[0] + '_starcoded.txt'
        p1 = subprocess.Popen(['cat', fname], stdout=subprocess.PIPE)
        p2 = subprocess.Popen([
            'starcode',
            '-t4',
            '-d2',
            '--print-clusters',
            '-o',
            starcodefn],
            stdin=p1.stdout,
            stdout=subprocess.PIPE)

        # 'communicate()' returns a tuple '(stdoutdata, stderrdata)'.
        # If 'stderrdata' is not None we notify.
        stdoutdata, stderrdata = p2.communicate()
        if stderrdata is not None:
            sys.stderr.write("Pipe error (%s)\n" % str(stderrdata))
