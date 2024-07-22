#!/usr/bin/env python3
'''

'''
import re 

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

print('first part')
for acc in accessions:
    if re.search(r"5", acc):
        print("\t" + acc)

print()
print('second part')
for acc in accessions:
    if re.search(r"[de]", acc):
        print("\t" + acc)

print() 
print('third part')
for acc in accessions:
    if re.search(r"d.*e", acc): # . any characters * zero or more times
        print("\t" + acc)

print() 
print('fourth part') 
for acc in accessions:
    if re.search(r"d.e", acc): # . any single characters
        print("\t" + acc)

print() 
print('fifth part')
# d and e in any order
for acc in accessions:
    if re.search(r"d.*e", acc) or re.search(r"e.*d", acc): # . any characters * zero or more times
        print("\t" + acc)


print() 
print('sixth part') 
for acc in accessions:
    if re.search(r"^[xy]", acc): # starts with x or y
        print("\t" + acc)

print() 
print('seventh part') 
for acc in accessions:
    if re.search(r"^[xy]", acc) and re.search(r"e$", acc): # . any characters * zero or more times
        print("\t" + acc)

print() 
print('eight part') 
for acc in accessions:
    if re.search(r"\d{3,}", acc): # . any characters * zero or more times
        print("\t" + acc)

print() 
print('nineth part') 
for acc in accessions:
    if re.search(r"d[arp]$", acc): # . any characters * zero or more times
        print("\t" + acc)


