'''
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]
说明:

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
'''

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        寻常n*n 肯定超时 可以考虑二分法 
        这里使用字典试试
        """
        list_nums2 = set(nums2)
        dict_nums2 = dict(zip(list_nums2, [0] * len(list_nums2)))
        res = []
        for n in set(nums1):
            if n in dict_nums2:
                res.append(n)
        return res