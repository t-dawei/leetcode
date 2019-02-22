'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        思路：
            每一个字符 从中间散开判断
        """
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        max_str = ''
        for x in range(len(s)):
            # palindrome like 'aba'
            temp = helper(s, x, x)
            max_str = (max_str, temp)[len(temp) > len(max_str)]
            # palindrome like 'abba'
            temp = helper(s, x, x+1)
            max_str = (max_str, temp)[len(temp) > len(max_str)]
        return max_str