#!/usr/bin/python
# -*- coding: utf-8 -*-


C = int(input())
for c in range(C):
	M, N = map(int, input().split())
	if M < N:
		M, N = N, M
	res = 1
	while True:
		if M%N == 0:
			break
		else:
			if M - N > N:
				break
			else:
				M, N = N, M-N
				res = ~res
	if res == 1:
		print('Stan wins')
	else:
		print('Ollie wins')
