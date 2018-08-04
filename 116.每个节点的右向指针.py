# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:57:52 2018
每个节点的右向指针:
给定一个二叉树
struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。
说明:
你只能使用额外常数空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
你可以假设它是一个完美二叉树（即所有叶子节点都在同一层，每个父节点都有两个子节点）。
----------------------------------------------------------------------------
示例:
给定完美二叉树，

     1
   /  \
  2    3
 / \  / \
4  5  6  7
调用你的函数后，该完美二叉树变为：

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
@author: Wan G.S
"""
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        stack = [root]
        while stack:
            temp = []
            for node in stack:
                if node:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
            for i, node in enumerate(temp[:-1]):
                node.next = temp[i+1]
            stack = temp
