'''
给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。

返回 A 的任意排列，使其相对于 B 的优势最大化。

 

示例 1：

输入：A = [2,7,11,15], B = [1,10,4,11]
输出：[2,11,7,15]
示例 2：

输入：A = [12,24,8,32], B = [13,25,32,11]
输出：[24,32,8,12]
 

提示：

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
'''
	
# 超时
class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A = list(sorted(A))
        B = list(sorted(B))
        list_res = []
        for i, b in enumerate(B):
            for j in range(i, len(A)):
                if A[j] > b:
                    list_res.append(A[j])
                    break
            else:
                list_res += A[i:]
        return list_res

# 方法2
    def advantageCount(self, A, B):
        A = sorted(A)
        take = collections.defaultdict(list)
        for b in sorted(B)[::-1]:
            if b < A[-1]: take[b].append(A.pop())
        return [(take[b] or A).pop() for b in B]