'''
给定一个树，按顺序重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

 

示例 ：

输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
 

提示：

给定树中的结点数介于 1 和 100 之间。
每个结点都有一个从 0 到 1000 范围内的唯一整数值。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        # 树的中序遍历//----> 栈
        """
        # 树的中序遍历（递归方法）
        def mid_trans(root):
            res = []
            if root:
                res += mid_trans(root.left)
                res.append(root.val)
                res += mid_trans(root.right)
            return res
        res = mid_trans(root)
        new_res = []
        for r in res:
            new_res.append(r)
            new_res.append(None)
        new_res.pop()
        return new_res