rows = [
    {'address' : '5412 N ClARK', 'date': '07/01/2012'},
    {'adresses': '5148 N CLARK', 'date': '07/0412012'},
    {'adresses': '5800 N 58TH', 'date':  '07/02/2012'},
    {'address': '2122 N CLARK',  'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1639 N GRANVILLE', 'date': '07/04/2012'}
]
from itertools import groupby

#rows.sort(key=lamda r: r['date'])
for date, items in groupby(rows, key=lambda r: r['date']):
    print(date)
    for i in items:
        print('     ', i)
        
# Example of building a multidict
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print (r)