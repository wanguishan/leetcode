# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 13:22:10 2018
删除链表的倒数第N个节点:
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
-----------------------------------------------------------------
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
@author: Wan G.S
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for _ in range(n):
            p2 = p2.next
            
        while p2.next:
            p2 = p2.next
            p1 = p1.next
            
        p1.next = p1.next.next
        return dummy.next


    def removeNthFromEnd_2(self, head, n):
        p1 = p2 = head
        for _ in range(n):
            p2 = p2.next
        if not p2:
            return head.next
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        p1.next = p1.next.next
        return head