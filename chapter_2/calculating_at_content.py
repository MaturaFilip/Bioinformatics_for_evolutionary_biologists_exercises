#!/usr/bin/env python3
'''
Calculating AT content in selected DNA sequence
'''

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

seq_len = len(seq)
a_count = seq.count('A')
t_count = seq.count('T')

at_count = a_count + t_count

print(f"AT content: {at_count/seq_len:.2f}")
