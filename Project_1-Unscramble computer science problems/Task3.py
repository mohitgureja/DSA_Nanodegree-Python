"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

numbers_set = set()

def get_num_called(calls):
	count_bnglr = 0
	count_all = 0
	for call in calls:
		if(call[0].startswith('(080)')) :
			count_all += 1
			if(call[1].startswith('(')):
				string = re.search(r"(\([0-9]+\))",call[1])
				prefix = string.group(1)
				if(prefix == '(080)'):
					count_bnglr += 1
			elif(call[1][0] == '7' or call[1][0] == '8' or call[1][0] == '9'):
				prefix = call[1][0:4]
			elif(call[1].startswith('140')):
				prefix = '140'
			
			numbers_set.add(prefix)
	return count_bnglr, count_all


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

count_bnglr, count = get_num_called(calls)
print ("The numbers called by people in Bangalore have codes:")
for number in sorted(numbers_set):
	print (number)

print (f"{((count_bnglr*100)/count):.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
