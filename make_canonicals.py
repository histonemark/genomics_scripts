#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import re
import sys
import subprocess

for fname_mapped in os.listdir("."):
    try:
        if not fname_mapped.split("_")[1] == 'mapped.txt':
            continue
        fname_starcoded = re.sub(r'\_mapped.txt$', '_canonicals.txt', fname_mapped)
        p1 = subprocess.Popen(['cut', '-f1', fname_mapped],
                                  stdout=subprocess.PIPE)
        p2 = subprocess.Popen([
            'starcode',
            '-t4',
            '-d2',
            '--print-clusters',
            '-o',
            fname_starcoded],
            stdin=p1.stdout, stdout=subprocess.PIPE)
        # 'communicate()' returns a tuple '(stdoutdata, stderrdata)'.
        # If 'stderrdata' is not None we notify to know where the problem arose.
        stdoutdata,stderrdata = p2.communicate()
        if stderrdata is not None:
            sys.stderr.write("Pipe error (%s)\n" % str(stderrdata))
    except IndexError:
        continue
