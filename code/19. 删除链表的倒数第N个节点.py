'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head
        list_res = []
        num = 0
        while cur != None:
            num += 1
            list_res.append(cur)
            cur = cur.next
        
        if n == num:
            return head.next
        elif n == 1:
            pre_data = list_res[num-n-1]
            pre_data.next = None
            return head
        else:
            pre_data = list_res[num-n-1]
            pre_data.next = list_res[num-n].next
            return head