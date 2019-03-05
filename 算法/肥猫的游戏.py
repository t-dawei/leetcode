#!/usr/bin/python
# -*- coding: utf-8 -*-

n = int(input())
list_d = [0 for i in range(n+1)]
a, b, c = map(int, input().split())
list_d[a] = list_d[b] = list_d[c] = 1
res = 0
for i in range(n-3):
	a, b, c = map(int, input().split())
	if list_d[a] + list_d[b] + list_d[c] == 2:
		res += 1
if res == 1:
	print('JMcat Win')
else:
	if n % 2 == 0:
		print('JMcat Win')
	else:
		print('PZ Win')
	

