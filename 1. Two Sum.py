'''
# question
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# answer 1
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        思路：
            相减
        """
        for x in range(len(nums)):
            sub_nums = nums[x+1:]
            if target-nums[x] in sub_nums:
                index = sub_nums.index(target-nums[x])
                print(x, index + x + 1)
                return [x, index + x + 1]
		
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        思路：
            相减
            字典保存
        """
        dict_buff = {}
        for k, value in enumerate(nums):
            if value in dict_buff:
                return [dict_buff[value], k]
            else:
                dict_buff[target-value] = k
   		

if __name__ == '__main__':
	Solution().twoSum2([2, 7, 11], 9)
