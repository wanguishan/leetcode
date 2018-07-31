# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:47:48 2018
对称二叉树:
给定一个二叉树，检查它是否是镜像对称的。
--------------------------------------------------------------------
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
@author: Wan G.S
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        思路一：递归
        """
        def isMirror(left, right):
            if not left and not right:
                return True
            elif left and right and left.val == right.val:
                outPair = isMirror(left.left, right.right)
                inPair = isMirror(left.right, right.left)
                return outPair and inPair
            else:
                return False
            
        if not root:
            return True
        return isMirror(root.left, root.right)
    
    
    def isSymmetric_2(self, root):
        """
        思路二：迭代
        """    
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            elif left and right and left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True

