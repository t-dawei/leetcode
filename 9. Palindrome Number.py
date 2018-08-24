'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        思路：
            利用求模取每位数字
        """
        if x < 0:
            return False
        else:
            list_res = []
            res = x
            while res > 0:
                left = res % 10
                res = res // 10
                list_res.append(left)
            list_copy = list_res.copy()
            list_copy.reverse()
            return list_res == list_copy