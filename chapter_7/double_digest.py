#!/usr/bin/env python3
'''
dna.txt -> predict fragment lengths after digesting with AbcI ANT*AAT and AbcII GCRW*TG

* == cut site
'''
import re

with open('dna.txt', 'r') as f:
    seq = f.read()

all_cuts = [0]

# add cut positions for AbcI
for match in re.finditer(r'A[ATGC]TAAT', seq):
    all_cuts.append(match.start() + 3) 


# add cut positions for AbcII
for match in re.finditer(r'GC[AG][AT]TG', seq):
    all_cuts.append(match.start() + 4)

# add final position
all_cuts.append(len(seq))
sorted_cuts = sorted(all_cuts)
print(sorted_cuts)

for i in range(1, len(sorted_cuts)):
    this_cut_position = sorted_cuts[i]
    previous_cut_position = sorted_cuts[i-1]
    fragment_size = this_cut_position - previous_cut_position
    print(f'Fragment size is {fragment_size}')

