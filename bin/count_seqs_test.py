#!/usr/bin/env python

import seq_utils
import sys

filename = 'python.fasta'
try:
  input_file = open(filename)
except IOError as e:
  print >>sys.stderr, "Error opening file {}: {}".format(filename, e.strerror)
else:
  seq_count = seq_utils.count_seqs(input_file)
  assert seq_count == 94
  print seq_count,"in",filename
