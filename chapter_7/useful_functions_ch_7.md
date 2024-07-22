# Useful functions from chapter 7: Regular expressions from book Python for biologists

import re
re.search(pattern, string) # true vs false

if re.search(r"GAATTC", dna):
	print("restriction site found")

re.search() can find pattern everywhere
re.match() can find pattern which matches **entire** entire string

## what part matches
re.search + group method

### store the match object in the variable m
m = re.search(r"GA[ATGC]{3}AC", dna)
print(m.group()) # print match pattern

## Getting the position of a match
method which give us position of start and end of the match
- str(m.start())
- str(m.end())

## Splitting a string using a regular expression
- re.split()

-> Split if we have more than ATGC
re.split(r"[^ATGC]", dna) # it make a list of dna parts

## Finding multiple matches
re.match() | re.search() -> only first match

multiple match -> re.findall()
- output of finall is not match object, but list of strings # we can't extract positions

- re.finditer (we can extract positions)

for match in runs:
	run_start = match.start() # here we can use .match(), finditer returns a sequence of match objects
