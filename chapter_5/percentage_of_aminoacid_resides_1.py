#!/usr/bin/env python3
'''
'''

def per_aa_residues(prot_seq, aa):
    seq_len = len(prot_seq)
    aa_count = prot_seq.count(aa.upper())
    res_percentage = round((aa_count / seq_len) * 100)
    return res_percentage

assert per_aa_residues("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert per_aa_residues("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert per_aa_residues("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert per_aa_residues("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
