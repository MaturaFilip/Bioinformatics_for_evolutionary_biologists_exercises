#!/usr/bin/env python3
'''
Section of genomics DNA + exons position with list (start, stop) -> save only exons
'''

with open('genomic_dna.txt') as f:
    genomic_dna_unfiltered = f.read()

print(genomic_dna_unfiltered)

exons_only = ""

with open('exons.txt') as f:
    for line in f:
        positions = line.split(',')
        start = positions[0]
        stop = positions[1]
        exons_only += genomic_dna_unfiltered[int(start):int(stop)]

with open('coding_sequence.txt', 'w') as f:
        f.write(exons_only)


# map(function, iterable)


# with map function
#combined_exons = ""
#with open('exons.txt', 'r') as f:
 #   for line in f:
  #      start, end = map(int, line.split(','))
   #     combined_exons += genomic_sequence[start-1:end]


