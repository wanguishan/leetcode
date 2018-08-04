# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:41:53 2018
从前序与中序遍历序列构造二叉树：
根据一棵树的前序遍历与中序遍历构造二叉树。
-----------------------------------------------------------------------------
注意:
你可以假设树中没有重复的元素。
例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
@author: Wan G.S
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        val = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:val+1], inorder[:val])
        root.right = self.buildTree(preorder[val+1:], inorder[val+1:])
        return root
