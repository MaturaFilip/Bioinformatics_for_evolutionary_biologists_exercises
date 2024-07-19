#!/usr/bin/env python3
'''
Open text file genomic_dna.txt and split it into coding and non coding sequences based on exercises in chapter 2
'''

file_with_seq = open('genomic_dna.txt')
seq = file_with_seq.read()

exon_1 = seq[:62]
exon_2 = seq[90:]
intron = seq[62:90]

# write exons 
exons = open('exons.txt', 'w')
exons.write(exon_1 + exon_2)
exons.close()

# write intron
intron_file = open('intron.txt', 'w')
intron_file.write(intron)
intron_file.close()
