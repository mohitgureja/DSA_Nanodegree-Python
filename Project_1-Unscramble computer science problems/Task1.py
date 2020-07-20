"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
number_set = set()

def unique_num(number_file):
    with open(number_file, 'r') as f:
        reader = csv.reader(f)
        numbers_list = list(reader)
        for number in numbers_list:
        	number_set.add(number[0])
        	number_set.add(number[1])

unique_num('texts.csv')
unique_num('calls.csv')

print (f"There are {len(number_set)} different telephone numbers in the records.")
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
