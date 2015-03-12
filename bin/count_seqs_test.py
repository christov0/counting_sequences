#!/usr/bin/env python

import seq_utils

filename = 'python.fasta'
input_file = open(filename)
seq_count = seq_utils.count_seqs(input_file)
print seq_count,"in",filename
