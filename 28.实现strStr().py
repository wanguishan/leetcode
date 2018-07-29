# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 13:04:26 2018
实现strStr():
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回 -1。
------------------------------------------------------------------------------
示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1
@author: Wan G.S
"""
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)    ##python内置函数 find()
    
    
    def strStr_2(self, haystack, needle):
        if not needle:
            return 0
        length = len(needle)
        for i in range(len(haystack) - length + 1):
            if haystack[i:i + length] == needle:
                return i
        return -1