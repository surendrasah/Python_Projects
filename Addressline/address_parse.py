"""
An address provider returns addresses only with concatenated street names and numbers.
Our own system on the other hand has separate fields for street name and street number.

Input: string of address

Output: string of street and string of street-number as JSON object

A simple python program that does the task for the most simple cases, e.g.

"Winterallee 3" -> {"street": "Winterallee", "housenumber": "3"}
"Musterstrasse 45" -> {"street": "Musterstrasse", "housenumber": "45"}
"Blaufeldweg 123B" -> {"street": "Blaufeldweg", "housenumber": "123B"}
Consider more complicated cases

"Am Bächle 23" -> {"street": "Am Bächle", "housenumber": "23"}
"Auf der Vogelwiese 23 b" -> {"street": "Auf der Vogelwiese", "housenumber": "23 b"}
Consider other countries (complex cases)

"4, rue de la revolution" -> {"street": "rue de la revolution", "housenumber": "4"}
"200 Broadway Av" -> {"street": "Broadway Av", "housenumber": "200"}
"Calle Aduana, 29" -> {"street": "Calle Aduana", "housenumber": "29"}
"Calle 39 No 1540" -> {"street": "Calle 39", "housenumber": "No 1540"}

"""

import re
import json

class AddressLine():

	def parse_simple_address(self, address):

		match_address = address.split()
		if match_address:
			street = ' '.join(match_address[:-1])
			housenumber = match_address[-1]
			return json.dumps({'street': street, 'housenumber': housenumber})

		else:
			return "sorry, the address can not be parsed"

		
	def parse_complicated_address(self, address):

		match = re.match(r'(.+?)\s+(\d.*)', address)
		if match:
			street = match.group(1)
			housenumber = match.group(2)

			#ensure_ascii=False for JSON storing Unicode characters as it is (e.g. ä)
			return json.dumps({'street': street.strip(', '), 'housenumber': housenumber},ensure_ascii=False)

		else:
			return "sorry, the address can not be parsed"


	def parse_complex_address(self, address):

		match_withstring = re.search(r'([^\d]+)\s(\d+)', address)
		match_withdigit = re.match(r'\d+', address)
		match_withno = re.search(r'No \d+', address)  # Calle 39 No 1540

		#address having No XX
		if match_withno:
			housenumber = match_withno.group()
			street = address[:match_withno.start()]

		#address starting with string
		elif match_withstring:
			street = match_withstring.group(1)
			housenumber = match_withstring.group(2)

		#address starting with digit
		elif match_withdigit:
			housenumber = match_withdigit.group()
			street = address[match_withdigit.end():]

		else:
			return "sorry, the address can not be parsed"

		return json.dumps({'street': street.strip(', '), 'housenumber': housenumber})



if __name__=='__main__':
	addressline = AddressLine()
	# Test the function with given example addresses
	print(addressline.parse_simple_address("Winterallee 3"))
	print(addressline.parse_simple_address("Musterstrasse 45"))
	print(addressline.parse_simple_address("Blaufeldweg 123B"))
	print(addressline.parse_complicated_address("Am Bächle 23"))
	print(addressline.parse_complicated_address("Auf der Vogelwiese 23 b"))
	print(addressline.parse_complex_address('4, rue de la revolution'))
	print(addressline.parse_complex_address('200 Broadway Av'))
	print(addressline.parse_complex_address('Calle Aduana, 29'))
	print(addressline.parse_complex_address('Calle 39 No 1540'))


