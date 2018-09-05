import itertools
string = '1122345678543'
for x, y in itertools.groupby(string):
	print(x,y)