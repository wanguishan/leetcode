# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:01:47 2018
验证二叉搜索树:
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
--------------------------------------------------------
示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
@author: Wan G.S
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorderTraversal(root):
            if root:
                res = []
                res += inorderTraversal(root.left)
                res.append(root.val)
                res += inorderTraversal(root.right)
                return res
            return []
        
        res = inorderTraversal(root)
        if res == sorted(list(set(res))):
            return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        