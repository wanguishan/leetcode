# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 22:40:16 2018
反转链表：
反转一个单链表。
------------------------------------
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
@author: Wan G.S
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        new_head = None
        while head:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp
        return new_head
             