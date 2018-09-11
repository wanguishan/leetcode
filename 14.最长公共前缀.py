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
        res = ''
        i = 0
        while True:
            try:
                temp = strs[0][i]
                for str in strs:
                    if str[i] != temp:
                        return res
            except:
                return res
            i += 1
            res += temp
        return res


    def longestCommonPrefix_2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        shortest = min(strs, key=len)    ## shortest = sorted(strs, key=len)[0]
        for i, ch in enumerate(shortest):
            for str in strs:
                if str[i] != ch:
                    return shortest[:i]
        return shortest



