# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 12:39:52 2018
环形链表：
给定一个链表，判断链表中是否有环。
@author: Wan G.S
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if  not head:
            return False
        p1 = p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False
