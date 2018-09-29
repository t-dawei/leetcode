'''
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

 

示例 1：

输入: piles = [3,6,7,11], H = 8
输出: 4
示例 2：

输入: piles = [30,11,23,4,20], H = 5
输出: 30
示例 3：

输入: piles = [30,11,23,4,20], H = 6
输出: 23
 

提示：

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9
'''

import math
class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        '''
        # 超时 咋办 -> 时间在哪 range(max_k) 如何处理？ 试试二分法
        k = max_k = max(piles)
        for i in range(max_k)[::-1]:
            num = 0
            for n in piles:
                num += math.ceil(n/i)
            if num > H:
                break
            else:
                k = i
        return k
        '''
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