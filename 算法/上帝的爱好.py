#!/usr/bin/python
# -*- coding: utf-8 -*-

N = int(input())
ine = [0 for i in range(10001)]
flag = [-2 for i in range(10001)]

t = ans = temp = 0
list_d = list(map(int, input().split()))
for n in hh:
	if ine[n] != t:
		flag[n] = 1
		ine[n] = t
	else:
		flag[n] = ~flag[n]
	if flag[n] == -2:
		temp += 1
	if temp == 2:
		t += 1
		ans += 1
		temp = 0
print(ans)
