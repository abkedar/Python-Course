import datetime

"""
This scriptss create an empty file.
"""

filename = datetime.datetime.now()

# create a empty file
def create_file():
	"""This function create an empty file"""
	with open(filename, "w") as file:
		file.write("")