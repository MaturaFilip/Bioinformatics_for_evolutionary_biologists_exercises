#!/usr/bin/env python3
"""
What percentage of the DNA sequence is coding
"""


seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon_1 = seq[:62]
exon_2 = seq[90:]

coding_length = len(exon_1 + exon_2)
total_length = len(seq)

print(f"Coding percentage: {(coding_length / total_length) * 100:.2f}")
