#!/usr/bin/python
# -*- coding: utf-8 -*-


import math
def num(data):
	count = 2
	if data == 1:
		return 1
	for i in range(2, math.floor(math.sqrt(data)+1)):
		if data%i == 0:
			if pow(i, 2) == data:
				count += 1
			else:
				count += 2
	return count
k = int(input())

res = []
for i in range(1, 2001):
	if num(i) == k:
		res.append(i)
if len(res):
	for i in res:
		print(i)
else:
	print('NO SOLUTION')

