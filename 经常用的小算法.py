
# ========================
# 求字符串重新排列的所有结果
# 思路：确定首位 然后递归确定第二位 再递归确定第三位... 跳出递归条件为输入s长度为1 
def perm(s):
	if len(s) == 1:
		return [s]

	list_string = []
	# 确定首位
	for x in range(len(s)):
		# 确定剩余部分
		for j in perm(s[:x] + s[x+1:]):
			list_string.append(s[x] + j)

	return list_string	

# =========================
# 判断一个数是否为2的整数幂
# 思路：2的整数幂在转化为2进制后 其首位都为1， 其余位都为0
#		利用比2的整数幂小1的数 进行与运算 结果为0 则为2的整数幂
def power2(data):
	res = data & (data-1)
	# print(type(res), res)
	return res == 0
	
if __name__ == '__main__':
	print(power2(4))

