# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 12:19:41 2018
二叉树的层次遍历：
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
-----------------------------------------------------------------------------
例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
@author: Wan G.S
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            res.append([node.val for node in stack])
            new_stack = []
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return res
            
