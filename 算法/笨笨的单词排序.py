#!/usr/bin/python
# -*- coding: utf-8 -*-


def cmp_(x, y, string):
	index = 0
	while index < min(len(x), len(y)):
		x_index = string.index(x[index])
		y_index = string.index(y[index])
		if x_index > y_index:
			return 1
		elif x_index < y_index:
			return 0
		index += 1
	if len(x) <= len(y):
		return 0
	else:
		return 1

d_string = input()
N = int(input())
list_data = []
for n in range(N):
	list_data.append(input())
way = int(input())


for i in range(len(list_data)-1):
	state_change = False
	for j in range(len(list_data)-i-1):
		if cmp_(list_data[j], list_data[j+1], d_string):
			list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
			state_change = True
	if not state_change:
		break

if way == 0:
	list_data = list_data[::-1]

for w in list_data:
	print(w)




