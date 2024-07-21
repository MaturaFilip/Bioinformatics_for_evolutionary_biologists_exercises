#!/usr/bin/env python3
'''   
Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200
'''

with open('data.csv', 'r') as f:
    for line in f.readlines():
        df = line.rstrip('\n').split(',')
        gene_name = df[2]
        seq = df[1]
        expr = df[3]

        a_content = seq.count('A')
        t_content = seq.count('T')
        at_content = ((a_content + t_content) / len(seq)*100)
        if at_content < 50 and int(expr) > 200:                                    
            print(df[2])

