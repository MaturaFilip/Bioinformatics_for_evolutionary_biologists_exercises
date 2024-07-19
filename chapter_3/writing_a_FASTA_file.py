#!/usr/bin/env python3
'''
FASTA example:

>sequence_name
ATCGAGGCGAGGGGCGCT

Create FASTA file for 3 sequences 
'''

fasta_file = open('sequences.fasta', 'w')
first = ">ABC123\nATCGTACGATCGATCGATCGCTAGACGTATCG\n"
second = ">DEF456\nactgatcgacgatcgatcgatcacgact\n"
second = second.upper()
third = ">HIJ789\n" + "ACTGAC-ACTGT--ACTGTA----CATGTG".replace('-', '')


fasta_file.write(first + second + third)
