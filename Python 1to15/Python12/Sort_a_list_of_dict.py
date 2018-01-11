rows = [
    {'fname': 'Brain', 'lname':'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'Alex',  'lname': 'Cleese', 'uid': 1005},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    
]
from operator import itemgetter

rows_by_fname = sorted(rows, key = itemgetter('fname'))
rows_by_uid = sorted(rows, key = itemgetter('uid'))

print("Sorted by fname:\n {0}".format(rows_by_fname))

print("Sorted by uid:\n{0}".format(rows_by_uid))

