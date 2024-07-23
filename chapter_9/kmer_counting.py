#!/usr/bin/env python3
'''

'''
import os
import sys


# command line arg to variables
kmer_size = int(sys.argv[1])
count_cutoff = int(sys.argv[2])

def split_dna(dna, kmer_size):
    kmers = []

    for start in range(0,len(dna)-(kmer_size-1),1):
        kmer = dna[start:start+kmer_size]
        kmers.append(kmer)
    return kmers


kmer_counts = {}

for file_name in os.listdir('.'):
    if file_name.endswith('.dna'):
        print(f'reading sequences from {file_name}')
        with open(file_name, 'r') as dna_file:
            for line in dna_file:
                dna = line.rstrip('\n')
                for kmer in split_dna(dna, kmer_size):
                    current_count = kmer_counts.get(kmer, 0)
                    new_count = current_count + 1
                    kmer_counts[kmer] = new_count

# kmer cutoff filter
for kmer, count in kmer_counts.items():
    if count > count_cutoff:
        print(f'{kmer}: {count}')
