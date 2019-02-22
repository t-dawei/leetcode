'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        cur = head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        
        if len(res) % 2 == 0:
            l, r = len(res) // 2 -1, len(res) // 2
        else:
            l, r = (len(res)-1)//2-1, (len(res)-1)//2+1
        while 0 <= l:
            print(res[l], res[r])
            if res[l] != res[r]:
                return False
            l, r = l-1, r+1
        return True 
    