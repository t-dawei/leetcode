'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", which the length is 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        思路：
            两次遍历 o(n*n) 常规思路
        """
        max_len = 0
        for x in range(len(s)):
            string, index = '', x
            while True:
                if s[index] in string:
                    max_len = (max_len, len(string))[len(string) > max_len]
                    break
                else:
                    string += s[index]
                    if index == len(s) - 1:
                        max_len = (max_len, len(string))[len(string) > max_len]
                        break
                index += 1
        return max_len

# 方法2 时间复杂度：O(n)
class Solution:
    # HashMap
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength