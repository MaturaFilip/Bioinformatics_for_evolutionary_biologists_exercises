#!/usr/bin/env python3
'''
Take DNA sequence and print the complement of this sequence
'''

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

complement_seq = ""

for i in seq:
    if i == "A":
        complement_seq += "T"
    elif i == "T":
        complement_seq += "A"
    elif i == "G":
        complement_seq += "C"
    elif i == "C":
        complement_seq += "G"
    else:
        complement_seq += "N"

print(f"Original sequence: {seq}")
print()
print(f"Complement sequence: {complement_seq}")
