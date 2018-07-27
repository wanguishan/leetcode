# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 16:33:32 2018
字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
-----------------------------------------------------------------------------------
案例:
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
@author: Wan G.S
"""
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
            
        for j in s:
            if dic[j] == 1:
                return s.index(j)

        return -1        


print(Solution().firstUniqChar('leetcode'))