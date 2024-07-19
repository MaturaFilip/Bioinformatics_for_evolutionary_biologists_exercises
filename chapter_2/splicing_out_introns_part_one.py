#!/usr/bin/env python3
"""
Sequence with 2 exons and 1 intron

1 exon: from start to the 63 character
2 exon from 91 to the end

Print only coding regions of the DNA sequence
"""

seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon_1 = seq[:62]
exon_2 = seq[90:]

print(f"Coding region: {exon_1 + exon_2}")
