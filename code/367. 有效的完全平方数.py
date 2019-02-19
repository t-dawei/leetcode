'''
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False
'''

import math
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        min_n, max_n = 1, math.ceil(num / 2)
        mid = (min_n + max_n) // 2
        flag = False
        while min_n <= max_n:
            # print(mid, min_n, max_n)
            if mid ** 2 > num:
                max_n = mid - 1
            elif mid ** 2 < num:
                min_n = mid + 1
            else:
                flag = True
                break
            mid = (min_n + max_n) // 2
        return flag