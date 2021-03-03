"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

phone_dict = {}
for row in calls:
    # check for calling number
    if row[0] in phone_dict:
        phone_dict[row[0]] += int(row[3])
    else:
        phone_dict[row[0]] = int(row[3])

    # check for receiving number
    if row[1] in phone_dict:
        phone_dict[row[1]] += int(row[3])
    else:
        phone_dict[row[1]] = int(row[3])

# find the maximum duration and the number with that duration
maximum_record = max(phone_dict.items(), key=lambda x: x[1])

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(maximum_record[0], str(maximum_record[1])))
