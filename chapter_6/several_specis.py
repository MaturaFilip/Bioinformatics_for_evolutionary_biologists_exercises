#!/usr/bin/env python3
'''
Print out gene names for all genes belonging to Drosophila melanogaster and Drosophila simulans
'''

with open('data.csv', 'r') as f:
    for line in f.readlines():
        df = line.rstrip('\n').split(',')
        if df[0] == 'Drosophila melanogaster' or df[0] == 'Drosophila simulans':
            print(df[0])
