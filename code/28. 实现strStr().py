'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 方法1
        # return (0, haystack.find(needle))[needle != '']
        
        # 方法2
        len_ = len(needle)
        if not len_:
            return 0
        else:
            for x in range(len_, len(haystack) + 1):
                if haystack[x-len_:x] == needle:
                    return x-len_
            else:
                return -1