#!/usr/bin/env python3
'''
Cut the adapters from beginning of the sequence (14 base pair fragment) and save it into new file
'''


cuted_seq = ""

file_with_seq = open('input.txt')
for line in file_with_seq:
    cuted_seq += line[14:] 

file_with_seq.close()

cuted_file = open('trimmed_seq.txt', 'w')
cuted_file.write(cuted_seq)
cuted_file.close()
