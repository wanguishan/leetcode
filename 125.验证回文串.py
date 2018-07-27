# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:48:54 2018
验证回文字符串:
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
----------------------------------------------------------------------------------
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
@author: Wan G.S
"""
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        phead, ptail = 0, len(s)-1
        while phead < ptail:
            if not s[phead].isalnum():
                phead += 1
            elif not s[ptail].isalnum():
                ptail -= 1
            else:
                if s[phead].lower() != s[ptail].lower():
                    return False
                else:
                    phead += 1
                    ptail -= 1
        return True       



    def isPalindrome_2(self, s):
        """
        同上，减少了嵌套循环
        """
        phead, ptail = 0, len(s)-1
        while phead < ptail:
            if not s[phead].isalnum():
                phead += 1
                continue
            if not s[ptail].isalnum():
                ptail -= 1
                continue
            if s[phead].lower() != s[ptail].lower():
                return False
            else:
                phead += 1
                ptail -= 1
        return True  
        
        
    
    
    def isPalindrome_3(self, s): 
        new = list(filter(str.isalnum, s.lower()))
        # new = [i.lower() for i in s if i.islanum()]
        return new == new[::-1]

s = "A man, a plan, a canal: Panama"   
print(Solution().isPalindrome_2(s))
