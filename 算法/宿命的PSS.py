#!/usr/bin/python
# -*- coding: utf-8 -*-


def get(d):
	if list_fa[d] == d:
		return d
	list_fa[d] = get(list_fa[d])
	return list_fa[d]

N = int(input())
list_e = []
for n in range(N-1):
	x, y, v = map(int, input().split())
	list_e.append((x,y,v))

list_e = sorted(list_e, key=lambda x:x[2], reverse=False)

# 表示节点i所在的组
list_fa = []
# 表示每个组的节点个数
num = []

for i in range(0, N+1):
	list_fa.append(i)
	num.append(1)

ans = 0
for e in list_e:
	index_x = get(e[0])
	index_y = get(e[1])
	ans += (num[index_x] * num[index_y] - 1) * (e[2] + 1) + e[2]
	num[index_x] += num[index_y]
	list_fa[index_y] = index_x

print(ans) 




