#!/usr/bin/env python3
'''   
Print out the gene names for all genes whose name begins with 'k' or 'h' except those belonging to Drosophila melanogaster
'''

with open('data.csv', 'r') as f:
    for line in f.readlines():
        df = line.rstrip('\n').split(',')  
        gene_name = df[2]
        species_name = df[0]
        if gene_name.startswith('k') or gene_name.startswith('h') and species_name != 'Drosophila melanogaster': 
            print(df[2])

