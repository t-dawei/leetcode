'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        思路：
        	先求和 再考虑进位
        """       
        head = cur = ListNode(0)
        while l1 and l2:
            cur.next = ListNode(l1.val + l2.val)
            cur, l1, l2 = cur.next, l1.next, l2.next
        cur.next = l1 or l2
        temp = head.next
        while temp:
            if temp.val >= 10:
                temp.val -= 10
                if temp.next:
                    temp.next.val += 1                   
                else:
                    temp.next = ListNode(1)
            temp = temp.next         
        return head.next


# 方法2 更加简洁
def addTwoNumbers(self, l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry //= 10
    return dummy.next