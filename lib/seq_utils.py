#!/usr/bin/env python

def count_seqs(input_file):
	count=0
	for line in input_file:
		line=line.strip() # strip any leading spaces
		if line.startswith(">"):
			count+=1
	return count
