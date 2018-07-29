# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 15:14:48 2018
回文链表:
请判断一个链表是否为回文链表。
------------------------------------------
示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true
@author: Wan G.S
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        思路一：快慢指针
        """
        p1 = p2 =head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            
        p1 = self.reverseList(p1)
        p2 = head
        while p1 and p2:
            if p1.val != p2.val:
                return False
            else:
                p1 = p1.next
                p2 = p2.next
        return True
        
        
    def reverseList(self, head):
        newHead = None
        while head:
            temp = head.next
            head.next = newHead
            newHead = head
            head = temp
        return newHead
    
    
    
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        思路二：列表
        """    
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]