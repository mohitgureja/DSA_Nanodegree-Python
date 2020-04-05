"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict
# with open('texts.csv', 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    call_dict = {}
    call_dict = defaultdict(lambda: 0, call_dict)
    max_Value = 0;
    for call in calls:
    	call_dict[call[0]] += int(call[3])
    	call_dict[call[1]] += int(call[3])
    	
    	if(call_dict[call[0]] > max_Value):
    		max_Value = call_dict[call[0]]
    		key_max = call[0]
    	if(call_dict[call[1]] > max_Value):
    		max_Value = call_dict[call[1]]
    		key_max = call[1]

    print (f"{key_max} spent the longest time, {max_Value} seconds, on the phone during September 2016.")
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

