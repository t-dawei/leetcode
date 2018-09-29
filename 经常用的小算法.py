
# ========================
# 求字符串重新排列的所有结果
# 思路：确定首位 然后递归确定第二位 再递归确定第三位... 跳出递归条件为输入s长度为1 
# ========================
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
# ========================
def power2(data):
	res = data & (data-1)
	# print(type(res), res)
	return res == 0

# ========================
# 归并排序思想:
# 利用归并排序的思想，先将两个数组排好序，然后比较两个数组的大小，
# 若第一个数组的元素小于第二个数组的元素，
# 则第一个数组的元素往后挪，反之，第二个数组的元素往后挪
# ========================
def guibingpaixu(list1, list2):

	len1 = len(list1)
	len2 = len(list2)
	p1 = p2 = 0
	res = []
	while  p1 < len1 and p2 < len2:
		if list1[p1] < list2[p2]:
			res.append(list1[p1])
			p1 += 1
		else list1[p1] >= list2[p2]:
			res.append(list2[p2])
			p2 += 1
	# res = res + list1[p1:] + list2[P2:]
	res += list1[p1:] or list2[P2:]
	return res
	


# ========================
# 二分查找
# ========================
def erfenchazhao():
	min_k, max_k = 1, max(piles)
    mid = (min_k + max_k) // 2
    while min_k != max_k:
        print(mid, min_k, max_k)
        num = 0
        for n in piles:
            num += math.ceil(n/mid)
        if num < H:
            # 注意这里不能 max_k = mid - 1
            max_k = mid
            mid = (min_k + max_k) // 2
        elif num > H:
            min_k = mid + 1
            mid = (min_k + max_k) // 2
        else:
            max_k = mid
            mid = (min_k + max_k) // 2
    return mid


# ========================
# 树 ---（深度优先） 先序遍历 中序遍历 后序遍历 ---- 递归算法与非递归算法
# ========================
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def pre_trans(root):
    res = []
    if root:
    	res.append(root.val)
        res += mid_trans(root.left)
        res += mid_trans(root.right)
    return res

def mid_trans(root):
    res = []
    if root:
        res += mid_trans(root.left)
        res.append(root.val)
        res += mid_trans(root.right)
    return res

def post_trans(root):
    res = []
    if root:
        res += mid_trans(root.left)
        res += mid_trans(root.right)
        res.append(root.val)
    return res

# 非递归遍历
def pre_trans_2(root):
	list_stack, res = [], []
	while root or list_stack:
		while root:
			res.append(root)
			list_stack.append(root)
			root = root.left
		if list_stack:
			root = list_stack.pop()
			root = root.right
	return res

def mid_trans_2(root):
	list_stack, res = [], []
	while root or list_stack:
		while root:
			list_stack.append(root)
			root = root.left
		if list_stack:
			root = list_stack.pop()
			res.append(root)
			root = root.right
	return res

def post_trans_2(root):
	list_stack, res = [], []
	pre = None
	list_stack.append(root)
	while list_stack:
		cur = list_stack[-1]
		# 如果当前结点没有子节点或者子节点都被访问了
		if (cur.left is None and cur.right is None) or ((pre is not None) and (pre == cur.left or pre == cur.right)):
		 	res.append(cur)
		 	list_stack.pop()
		 	pre = cur
		else:
			if cur.right is not None:
				list_stack.append(cur.right)
			if cur.left is not None:
				list_stack.append(cur.left)
	return res

# ========================
# 树 --- 层次遍历（广度优先）
# ========================
def level_trans(root):
	list_stack, res = [root], []
	while list_stack:
		cur = list_stack.pop()
		res.append(cur)
		if cur.left:
			list_stack.append(cur.left)
		if cur.right:
			list_stack.append(cur.right)
	return res

if __name__ == '__main__':
	print(power2(4))

