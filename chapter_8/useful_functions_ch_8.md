# Useful functions from chapter 8: Dictionaries from book Python for biologists


### how to add key:pair to empty dictionary
enzymes['EcoRI'] = r'GAATTC'

### delete from dict
enzymes.pop('EcoRI')

pretyprint for dict

### get method -> like looking for dict key print(counts['TGA']) but with second argument, what to print if the key not exist

print(f'count for TGA is {counts.get('TGA',0)}'

## Iterating over key
- print(counts.keys())

for trinucleotide in sorted(counts.keys()):
	if counts.get(trinucleotide) == 2:
	print(trinucleotide)
