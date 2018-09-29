'''
给定一个N叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

例如，给定一个 3叉树 :


			1
		2	3	4
	5	6
 

我们应返回其最大深度，3。

说明:

树的深度不会超过 1000。
树的节点总不会超过 5000。
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        思路：深度遍历思想
        """
        if not root:
            return 0
        if not root.children:
            return 1
        return max([self.maxDepth(node) for node in root.children]) + 1