"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

def unique_num(data):
    """
    make unique numbers set

    input: data(list)
    output: unique numbers as set

    """
    all_num = set()
    for row in data:
        all_num.add(row[0])
        all_num.add(row[1])
    return all_num


uni_txt = unique_num(texts)
uni_call= unique_num(calls)
all_distinct_num = (uni_txt | uni_call)
print("There are {} different telephone numbers in the records.".format(str(len(all_distinct_num))))
