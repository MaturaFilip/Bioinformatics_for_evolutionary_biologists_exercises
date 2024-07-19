#!/usr/bin/env python3
'''
Coding bases in uppercase
Non-coding bases in lowercase
'''


seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon_1 = seq[:62]
exon_2 = seq[90:]
intron = seq[62:90]


print("Sequence with coding regions in uppercase and non-coding in lowercase")
print()
print(exon_1 + intron.lower() + exon_2)
