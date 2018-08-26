'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        思路：
            一位一位比较
        """
        string = ''
        if not strs:
            return string
        str_0 = strs[0]
        index = 0
        L = len(str_0)
        while index < L:
            s = str_0[index]
            for ss in strs:
                if ss[index:index+1] != s:
                    return string
            else:
                string += s
                index += 1
        return string