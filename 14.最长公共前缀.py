# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 20:48:47 2018
最长公共前缀:
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
-------------------------------------------------------------------
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
@author: Wan G.S
"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        i = 0
        while True:
            try:
                temp = strs[0][i]
                for item in strs:
                    if item[i] != temp:
                        return prefix
            except:
                return prefix
            prefix += temp
            i += 1
            
        return prefix
    
    
    def longestCommonPrefix_2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
        