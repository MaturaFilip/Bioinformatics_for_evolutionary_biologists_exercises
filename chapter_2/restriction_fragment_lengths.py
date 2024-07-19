#!/usr/bin/env python3
"""
Find sites for the EcoRI restriction enzyme (cuts motif G*AATTC [cut indicated by an asterisk])

Then calculate size of the two fragments
"""


seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

cut_seq = seq.find("GAATTC")

print(f"Original sequence: {seq}")
print(f"First part: {seq[:(cut_seq)+1]}")
print(f"Second part: {seq[(cut_seq)+1:]}")

print(f"Length of the first part is: {len(seq[:(cut_seq)+1])} nucleotides")
print(f"Length of the second part is: {len(seq[(cut_seq)+1:])} nucleotides")
