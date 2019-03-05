#!/usr/bin/python
# -*- coding: utf-8 -*-

while True:
	n, m = map(int, input().split())
	list_d = list(map(int, input().split()))
	max_d = max(list_d)
	sum_d = sum(list_d)


	def statue(mid, m):
		k, sum_ = 0, 0
		for data in list_d:
			if sum_ + data > mid:
				k += 1
				sum_ = data
			else:
				sum_ += data
			if k > m -1:
				return False
		return True

	l = max_d
	r = sum_d

	while l < r:
		mid = (l + r) // 2
		if statue(mid, m):
			r = mid
		else:
			l = mid + 1

	print(l)