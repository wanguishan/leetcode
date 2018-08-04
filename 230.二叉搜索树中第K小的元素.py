# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 18:46:50 2018
二叉搜索树中第K小的元素:
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
-------------------------------------------------------------------------
示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
@author: Wan G.S
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        i = 0
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                i += 1
                if i == k:
                     return node.val
                root = node.right




    def kthSmallest_2(self, root, k):
        res =  self.LDR(root)
        return res[k-1]
    def LDR(self, root):
        if not root:
            return []
        left = self.LDR(root.left)
        right = self.LDR(root.right)
        res = left + [root.val] + right
        return res
