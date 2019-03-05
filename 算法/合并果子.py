#!/usr/bin/python
# -*- coding: utf-8 -*-

def reSort(c, list_d):
	for i in range(len(list_d)):
		if list_d[i] < c:
			list_d.insert(i, c)
			return list_d
	else:
		list_d.append(c)
	return list_d

N = int(input())
list_d = list(map(int, input().split()))
list_d = sorted(list_d, reverse=True)
if N == 1:
	print(0)
else:
	sum_ = 0
	while len(list_d) > 1:
		x = list_d.pop()
		y = list_d.pop()
		sum_ = sum_ + x + y
		list_d = reSort(x + y, list_d)
	print(sum_)




