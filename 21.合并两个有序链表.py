# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 14:48:59 2018
合并两个有序链表:
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
----------------------------------------------------------------------------
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
@author: Wan G.S
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        :递归
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        newHead = None
        if l1.val < l2.val:
            newHead = l1
            newHead.next = self.mergeTwoLists(l1.next, l2)
        else:
            newHead = l2
            newHead.next = self.mergeTwoLists(l1, l2.next)
        return newHead

    def mergeTwoLists_2(self, l1, l2):
        """非递归"""
        dummy = ListNode(0)
        pre = dummy
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next

        if not l1:
            pre.next = l2
        if not l2:
            pre.next = l1
        return dummy.next


    def mergeTwoLists_3(self, l1, l2):
        res = []
        while l1:
            res.append(l1.val)
            l1 = l1.next
        while l2:
            res.append(l2.val)
            l2 = l2.next
        res.sort()

        dummy = ListNode(0)
        pre = dummy
        for i in res:
            pre.next = ListNode(i)
            pre = pre.next
        return dummy.next