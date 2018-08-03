# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:46:23 2018
相交链表:
编写一个程序，找到两个单链表相交的起始节点。
--------------------------------------------------------------------------------
例如，下面的两个链表：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
在节点 c1 开始相交。
@author: Wan G.S
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        >时间复杂度O(m + n)
        >空间复杂度为O(m + n)
        """
        if not headA or not headB:
            return
        stack1 = []
        stack2 = []
        while headA:
            stack1.append(headA)
            headA = headA.next
        while headB:
            stack2.append(headB)
            headB = headB.next

        first = None
        while stack1 and stack2:
            top1 = stack1.pop()
            top2 = stack2.pop()
            if top1 is top2:
                first = top1
        return first


    def getIntersectionNode_2(self, headA, headB):
        """
        >时间复杂度O(m+n)
        >空间复杂度O(m+n)
        """
        length1 = self.GetListLength(headA)
        length2 = self.GetListLength(headB)
        if length1 > length2:
            headLong = headA
            headShort = headB
        else:
            headLong = headB
            headShort = headA
        diff = length1 - length2 if length1>length2 else length2-length1

        for i in range(diff):
            headLong = headLong.next

        while headLong != None and headShort != None and headLong != headShort:
            headLong = headLong.next
            headShort = headShort.next
        return headLong

    def GetListLength(self, pHead):
        length = 0
        while pHead:
            length += 1
            pHead = pHead.next
        return length

