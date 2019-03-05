#!/usr/bin/python
# -*- coding: utf-8 -*-

n =  int(input())

if 1 <= n <= 9:
	print('181818181818')
else:
	mul = 1
	while True:
		if (9 * mul) < n <= (18 * mul):
			print('ZBT') 
			break
		if (18 * mul) < n <= (9 * 18 * mul):
			print('181818181818')
			break
		mul *= 18
