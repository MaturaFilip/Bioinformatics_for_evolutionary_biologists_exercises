#!/usr/bin/env python3
'''   
gene name + AT content high than 0.65, low less than 0.45 or medium between 0.45 and 0.65
'''


def at_content(seq):
    seq_len = len(seq)
    a_count = seq.upper().count('A')
    t_count = seq.upper().count('T')
    at_content = (a_count + t_count) / seq_len
    return at_content

with open('data.csv', 'r') as f:
    for line in f.readlines():
        df = line.rstrip('\n').split(',')  
        seq = df[1]
        gene_name = df[2]
        if at_content(seq) > 0.65:
            print(f'name: {gene_name}; AT content high: {at_content(seq)}')
        elif at_content(seq) < 0.45:
            print(f'name: {gene_name}; AT content low: {at_content(seq)}')
        elif at_content(seq) < 0.65 and at_content(seq) > 0.45:
            print(f'name {gene_name}; AT content medium: {at_content(seq)}')
        else:
            print('wrong input')
