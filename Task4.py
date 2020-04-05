"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

def get_telemarketers(remove_set,calls_list):
	number_set = set()
	for number in calls_list:
		if(number[0] not in remove_set):
			number_set.add(number[0])
	return number_set

def get_removable_telemarketers(texts_list,calls_list):
	number_set = set()
	for number in texts_list:
		number_set.add(number[0])
		number_set.add(number[1])

	for number in calls_list:
		number_set.add(number[1])

	return number_set

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

number_set = get_telemarketers(get_removable_telemarketers(texts,calls),calls)
print ("These numbers could be telemarketers: ")
for number in number_set:
	print (number)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""