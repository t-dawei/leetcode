'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        思路：
            利用栈 每个元素入栈 匹配消除
        """
        list_valid = ['()', '[]', '{}']
        list_stack = []
        for w in s:
            if list_stack:
                string = list_stack[-1] + w
                if string in list_valid:
                    list_stack.pop(-1)
                else:
                    list_stack.append(w)
            else:
                list_stack.append(w)
        return len(list_stack) == 0