# example.py
#
#Example of calculating with dictionaries

prices = {
    'ACME' : 45.23,
    'ACPL' : 612.78,
    'IBM'  : 205.55,
    'HPQ'  : 37.20,
    'FB'   : 10.75
}

# find min and max price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

# print max and min values
print ('min Price:{0}'.format(min_price))
print ('max Price:{0}'.format(max_price))
       
print ('sorted prices:')
print_sorted = sorted(zip(prices.values(), prices_keys()))
for price, name in price_sorted:
    print('     ', prices, name)