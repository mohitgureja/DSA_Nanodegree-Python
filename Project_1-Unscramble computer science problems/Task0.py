import csv

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)[0]
    print(f'First record of texts, {texts[0]} texts {texts[1]} at time {texts[2]}')

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    call = calls[-1]
    print(f'Last record of calls, {call[0]} calls {call[1]} at time {call[2]}, lasting {call[3]} seconds')
"""
TASK 0:
What is the first reocrd of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

