# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 20:35:23 2018
两数相加:
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
--------------------------------------------------------------
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
@author: Wan G.S
"""
# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        _l1 = _l2 = ''
        while l1:
            _l1 += str(l1.val)
            l1 = l1.next
        while l2:
            _l2 += str(l2.val)
            l2 = l2.next
        res = str(int(_l1[::-1])+int(_l2[::-1]))[::-1]

        dummy = ListNode(0)
        temp = dummy
        for i in res:
            node = ListNode(i)
            temp.next = node
            temp = temp.next
        return dummy.next
