# Example of extracting a subset from a dictionary
from pprint import pprint

prices = {
    'ACME' : 45.23,
    'AAPL' : 612.78,
    'IBM'  : 205.55,
    'HPQ'  : 37.20,
    'FB'   : 10.75
}

# Make a dictionary of all prices over 200
pl= {key:value for key, value in prices.items() if value > 200}

print ("All prices over 200")
print (pl)

# Make a dictionary of tech stocks
tech_name = {'APPL', 'IBM', 'HPQ', 'MSFT'}
p2  = {key:value for key, value in prices.items() if kye in tech_name}

print("All techs")
pprint(p2)