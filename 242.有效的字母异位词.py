# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:11:55 2018
有效的字母异位词:
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
-----------------------------------------------------------------------------
示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false
@author: Wan G.S
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) != len(s):
            return False
        c = set(t)
        for i in c:
            if t.count(i) != s.count(i):
                return False
        return True
    
    def isAnagram_2(self, s, t):
        dic_s, dic_t = {}, {}
        for i in s:
            dic_s[i] = dic_s.get(i, 0) + 1
        for j in t:
            dic_t[j] = dic_t.get(j, 0) + 1
        return dic_s == dic_t        


if __name__ == '__main__':
    s = 'wanguishan'
    t = 'guishanwan'
    print(Solution().isAnagram(s, t))
    print(Solution().isAnagram_2(s, t))