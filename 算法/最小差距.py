#!/usr/bin/python
# -*- coding: utf-8 -*-


T = int(input())
for t in range(T):
	n = int(input())
	list_d = list(map(str, input().split()))
	list_d = sorted(list_d)
	res = float('inf')
	if n == 2:
		print(abs(int(list_d[0]) - int(list_d[1])))
	elif n % 2 == 1:
		if list_d[0] == '0':
			list_d[0], list_d[1] = list_d[1], list_d[0]
		new_d = list_d[1:]
		x = list_d[0] + ''.join(new_d[:int(len(new_d)/2)])
		y = ''.join(list_d[int(len(new_d)/2+1):][::-1])
		res = abs(int(x)-int(y))
		print(res)
	else:
		for d in range(len(list_d)-1):
			if list_d[d] != '0':
				new_d = list_d[:d] + list_d[d+2:]
				x = list_d[d] + ''.join(new_d[int(len(new_d)/2):][::-1])
				y = list_d[d+1] + ''.join(new_d[:int(len(new_d)/2)])
				absxy = abs(int(x)-int(y))
				res = absxy if absxy < res else res
		print(res)


