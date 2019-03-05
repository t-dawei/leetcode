#!/usr/bin/python
# -*- coding: utf-8 -*-


N = int(input())
for n in range(N):
	y, m, d = map(int, input().split())
	if m == 9 and d == 30:
		print('YES')
	elif m == 1 and d == 30:
		print('YES')
	elif (m + d)%2 == 0:
		print('YES')
	else:
		print('NO')
