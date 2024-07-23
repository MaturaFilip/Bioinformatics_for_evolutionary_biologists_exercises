#!/usr/bin/env python3
'''
- Create 9 folders
    one for sequences between 100 and 199, theb 200 to 299 etc.

'''
import os

# create a new folder for each bin
for bin_lower in range(100,1000,100):
    bin_upper = bin_lower + 99
    bin_folder_name = str(bin_lower) + '_' + str(bin_upper)
    if not os.path.exists(bin_folder_name):
        os.mkdir(bin_folder_name)

seq_number = 1

for file_name in os.listdir('.'):
    if file_name.endswith('.dna'):
        print(f'\nreading sequences from {file_name}')
        with open(file_name, 'r') as f:

            for line in f:
                dna = line.strip('\n')
                length = len(dna)
                print(f'found a dna sequence with len {length}')

                for bin_lower in range(100,1000,100):
                    bin_upper = bin_lower + 99
                    if length >= bin_lower and length < bin_upper:

                        print(f'bin is {bin_lower} to {bin_upper}')
                        bin_folder_name = str(bin_lower) + '_' + str(bin_upper)
                        output_path = bin_folder_name + '/' + str(seq_number) + '.dna'
                        with open(output_path, 'w') as output:
                            output.write(dna)

                        seq_number += 1

