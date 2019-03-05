#!/usr/bin/python
# -*- coding: utf-8 -*-

while True:
	n = int(input())
	list_d = list(map(int, input().split()))

	if n == 1:
		print(list_d[0])
	else:
		list_sum = [float('-inf') for i in range(n)]
		list_sum[0]=list_d[0]
		for i in range(1, n):
			list_sum[i] = max(list_d[i], list_sum[i-1] + list_d[i])

		print(max(list_sum)) 
