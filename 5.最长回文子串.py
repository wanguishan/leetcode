# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:51:25 2018
最长回文子串:
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
---------------------------------------------------------------------------
示例 1：
输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
@author: Wan G.S
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = maxLen = 0
        for i in range(len(s)):
            for k in (0, 1):
                _start, _maxLen = self.build(s, i-k, i+1)
                if _maxLen > maxLen:
                    start, maxLen = _start, _maxLen
        return s[start: start+maxLen]

    def build(self, s, m, n):
        while m>=0 and n<len(s) and s[m]==s[n]:
            m -= 1
            n += 1
        return m+1, n-1-m

