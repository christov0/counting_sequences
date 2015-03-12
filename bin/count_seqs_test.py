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
  # not really the right thing to do when you've got an assert.
  try:    
    assert seq_count == 94, "Expected 94 sequences in python.fasta"
  except AssertionError:
    print >>sys.stderr, "I got the wrong value from count_seqs, got {} expected 94".format(seq_count)
  else:  
    print seq_count,"in",filename
