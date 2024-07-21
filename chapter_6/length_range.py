#!/usr/bin/env python3
'''   
'Print out the gene names for all genes between 90 and 110 bases long
'''

with open('data.csv', 'r') as f:
    for line in f.readlines():
        df = line.rstrip('\n').split(',')
        seq = df[1]
        if len(seq) > 90 and len(seq) < 110:
            print(df[2])

