# Example of differents ways to filter data

mylist = [1, 2, 10, -2, 3, -9, -5, 8, 4, 5]

# All positive number
pos = [n for n in mylist if n > 0]
print pos


# All positives values
neg = [n for n in mylist if n < 0]
print neg

# Negatives values clipped to 0
neg_clipp = [n if n > 0 else 0 for n in mylist]
print neg_clipp

# positive values clipped to 0
pos_clip = [n if n < 0 else 0 for n in mylist]
print pos_clipp

# Compressing example

addresses = [
    '5412 N CLARK',
    '5128 N CLARK',
    '5800 N 58TH',
    '2122 N CLARK',
    '5645 W REVENSWOOD',
    '1060 W ADDISON', 
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
a = list(compress(addresses, more5))
print (a)
