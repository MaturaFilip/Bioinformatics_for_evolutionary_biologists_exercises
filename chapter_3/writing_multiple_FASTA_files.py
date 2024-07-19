#!/usr/bin/env python3
'''
Instead of 1 FASTA file, create 3 (one per sequence)
'''

abc = open('ABC123.FASTA', 'w')
abc.write('>ABC123\nATCGTACGATCGATCGATCGCTAGACGTATCG')
abc.close()

def_seq = open('DEF456.FASTA', 'w')
def_seq.write('>DEF456\n' + 'actgatcgacgatcgatcgatcacgact'.upper())
def_seq.close()

hij = open('HIJ789.FASTA', 'w')
hij.write('>HIJ789\n' + 'ACTGAC-ACTGT--ACTGTA----CATGTG'.replace('-',''))
hij.close()
