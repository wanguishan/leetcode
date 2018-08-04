# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:39:32 2018
中序遍历二叉树：
给定一个二叉树，返回它的中序遍历。
----------------------------------------------------
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
@author: Wan G.S
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        递归
        """
        if not root:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right

    def inorderTraversal_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        栈
        """
        if not root:
            return []
        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res

