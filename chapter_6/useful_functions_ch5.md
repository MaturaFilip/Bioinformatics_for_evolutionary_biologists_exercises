# Useful functions from chapter 6 Conditional tests in book Python for biologists

Conditions aka T or F
- startswith('ATG') # if.accession.startswith('a'):
- endswith('TTT')
- .isupper()
- .islower()

- if our function return True or False, we can use it in different if/else statements
	- is_AT_rich('AAAAAA') -> True -> do something with the sequence

- if at_conent > 0.65:
	return True
  else:
  	return False


Better -> return > at_content > 0.65
