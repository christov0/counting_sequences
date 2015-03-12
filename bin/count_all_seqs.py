#!/usr/bin/env python

import sys
import glob
import seq_utils

mydir = sys.argv[1]

pattern = '*.fasta'
fullpath = mydir + '/' + pattern
filenames = glob.glob(fullpath)
cnt=0
for filedir in filenames:
	tmp_file=open(filedir)
	namesplit=filedir.partition(mydir)
	filename=namesplit[len(namesplit)-1]
	print filename,seq_utils.count_seqs(tmp_file)
	cnt+=1

if len(sys.argv)<1:
	print >>sys.stderr,"To use tester.py enter 'tester.py <filename>'"
	sys.exit(1)
